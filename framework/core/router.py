from typing import Dict, List, Callable, Tuple, Type, Optional
import inspect

from framework.models.route import Route
from framework.models.request import Request


class Router:
    routes: Dict[str, List[Route]] = {
        "GET": [],
        # "HEAD": [],
        # "OPTIONS": [],
        # "TRACE": [],
        "PUT": [],
        "DELETE": [],
        "POST": [],
        # "PATCH": [],
        # "CONNECT": [],
    }  # TODO: maybe make keys enums, extract these to configs

    def _get_param_types_sources(
        self, handler_func: Callable, path_params: List[str]
    ) -> Tuple[Dict[str, Type], Dict[str, str]]:
        sign = inspect.signature(handler_func)
        param_types = {
            key: sign.parameters[key].annotation for key in sign.parameters.keys()
        }
        param_sources = dict()
        for key in param_types.keys():
            if key in path_params:
                param_sources[key] = "path"
            elif param_types[key] == Request: # TODO: check for values in a sequence. extract to configs (INJECT_TYPES)
                param_sources[key] = "inject"
            else:
                param_sources[key] = "query"
        return param_types, param_sources

    def add_route(self, method: str, route: str, handler_func: Callable):
        segments = route.split("?")[0].split("/")
        param_positions = {
            idx: segments[idx][1:-1]
            for idx in range(len(segments))
            if segments[idx].startswith("{") and segments[idx].endswith("}")
        }
        param_types, param_sources = self._get_param_types_sources(
            handler_func, list(param_positions.values())
        )

        self.routes[method].append(
            Route(
                method=method,
                route=route,
                segments=segments,
                param_positions=param_positions,
                handler=handler_func,
                param_types=param_types,
                param_sources=param_sources,
            )
        )

    def _find_exact_match(self, method: str, route: str) -> Optional[Route]:
        for stored_route in self.routes[method]:
            if stored_route.route == route:
                return stored_route

    def _find_pattern_match(self, method: str, route: str) -> Optional[Tuple[Route, Dict[str, str]]]:
        segments = route.split("/")
        for stored_route in self.routes[method]:
            params = dict()
            if len(stored_route.segments) != len(segments):
                continue
            for idx in range(len(segments)):
                if stored_route.segments[idx] == segments[idx]:
                    continue
                if idx not in stored_route.param_positions:
                    break
                params[stored_route.param_positions[idx]] = segments[idx]
            else:
                return stored_route, params
        return None, None

    def find_handler(self, method: str, route: str) -> Tuple[Route, Optional[Dict[str, str]]]:
        match_ = self._find_exact_match(method, route)
        params = None
        if not match_:
            match_, params = self._find_pattern_match(method, route)
        if not match_:
            raise Exception("404 not found")  # TODO: custom exception
        return match_, params

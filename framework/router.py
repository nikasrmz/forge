from typing import Dict, List, Callable, Tuple, Type
import inspect

from framework.route import Route
from framework.request import Request


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
        self, 
        handler_func: Callable, 
        path_params: List[str]
    ) -> Tuple[Dict[str, Type], Dict[str, str]]:
        sign = inspect.signature(handler_func)
        param_types = {
            key: sign.parameters[key].annotation for key in sign.parameters.keys()
        }
        param_sources = dict()
        for key in param_types.keys():
            if key in path_params:
                param_sources[key] = "path"
            elif param_types[key] == Request:
                param_sources[key] = "inject"
            else:
                param_sources[key] = "query"
        return param_types, param_sources
            

    def add_route(self, method: str, route: str, handler_func: Callable):
        segments = route.split("/")
        param_positions = {
            idx: segments[idx][1:-1]
            for idx in range(len(segments))
            if segments[idx].startswith("{") and segments[idx].endswith("}")
        }
        param_types, param_sources = self._get_param_types_sources(handler_func, list(param_positions.values()))

        self.routes[method].append(
            Route(
                method=method,
                route=route,
                segments=segments,
                param_positions=param_positions,
                handler=handler_func,
                param_types=param_types,
                param_sources=param_sources
            )
        )

    def find_handler(self, route: str) -> Callable:
        pass

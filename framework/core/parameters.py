from typing import Dict, List

from framework.models.route import Route
from framework.models.request import Request

def get_query_params(path: str) -> Dict[str, List[str]]:
    query_params = dict()
    if "?" not in path:
        return query_params
    params_split = path.split("?")[1].split("&")
    for entry in params_split:
        key, val = entry.split("=")
        if key not in query_params:
            query_params[key] = []
        query_params[key].append(val)

    return query_params

def build_handler_kwargs(
        route: Route, 
        path_params: Dict[str, str], 
        request: Request
    ) -> Dict[str, str]:
    handler_kwargs = dict()
    query_params = get_query_params(request.path)
    # TODO: type checking/matching, casting and possible query param gathering, from list.
    for param, source in route.param_sources.items():
        if source == "path":
            handler_kwargs[param] = path_params[param]
        elif source == "inject":
            if route.param_types[param] == Request:
                handler_kwargs[param] = request
        else:
            handler_kwargs[param] = query_params[param]
    return handler_kwargs
    
    
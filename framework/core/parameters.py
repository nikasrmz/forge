from typing import Dict, List, get_origin

from framework.models.route import Route
from framework.models.request import Request

def build_handler_kwargs(
        route: Route, 
        path_params: Dict[str, str], 
        request: Request
    ) -> Dict[str, str]:
    handler_kwargs = dict()
    # TODO: type checking/matching, casting and possible query param gathering, from list.
    for param, source in route.param_sources.items():
        if source == "path":
            handler_kwargs[param] = path_params[param]
        elif source == "inject":
            if route.param_types[param] == Request:
                handler_kwargs[param] = request
        else:
            if get_origin(route.param_types[param]) == list:
                handler_kwargs[param] = request.query_params[param]
            else:
                handler_kwargs[param] = request.query_params[param][0]
    return handler_kwargs
    
    
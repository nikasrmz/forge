from typing import List, Callable

from framework.route import Route

class Router:
    routes: List[Route]

    def add_route(self, method: str, route: str, handler_func: Callable):
        pass

    def find_handler(self, route: str) -> Callable:
        pass

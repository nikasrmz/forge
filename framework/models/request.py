from typing import Dict, List, Any
from dataclasses import dataclass

from framework.models.body import Body


@dataclass(frozen=True)
class Request:
    method: str
    path: str
    http_version: str
    query_params: Dict[str, List[str]]
    headers: Dict[str, str]
    body: Body

    def get_header(self, header: str, default: Any = None):
        return self.headers.get(header, default)

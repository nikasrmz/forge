from dataclasses import dataclass
from typing import Dict, List, Callable, Type


@dataclass(frozen=True)
class Route:
    method: str
    route: str
    segments: List[str]
    param_positions: Dict[int, str]
    handler: Callable
    param_types: Dict[str, Type]
    param_sources: Dict[str, str]

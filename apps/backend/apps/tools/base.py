from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Tools:
    name: str
    description: str
    function: Callable[..., Any]
    risk_level : str = 'low'
    requires_approval : bool = False


#standard structure for every nexus tools
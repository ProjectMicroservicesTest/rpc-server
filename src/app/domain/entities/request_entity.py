from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RequestEntity:
    url: str
    method: str
    params: Optional[dict] = None
    data: Optional[dict] = None
    headers: Optional[dict] = None
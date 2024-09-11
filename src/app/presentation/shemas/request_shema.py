from typing import Optional
from pydantic import BaseModel


class RequestShema(BaseModel):
    path: str 
    method: str
    params: Optional[dict] = None
    data: Optional[dict] = None
    headers: Optional[dict] = None
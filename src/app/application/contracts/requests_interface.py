from typing import Protocol, Self
from abc import abstractmethod

from src.app.domain.entities.request_entity import RequestEntity


class RequestsInterface(Protocol):
    @abstractmethod
    async def make_request(self: Self, request: RequestEntity) -> None:
        raise NotImplementedError
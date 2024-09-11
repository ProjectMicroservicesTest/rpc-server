from typing import Protocol, Self
from abc import abstractmethod


class ResolverInterface(Protocol):
    @abstractmethod
    def  resolve(self: Self, service_name: str) -> str:
        raise NotImplementedError
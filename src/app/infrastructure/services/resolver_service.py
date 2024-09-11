from typing import Self

from src.app.application.contracts.resolver_interface import ResolverInterface
from src.app.main.config import HostsConfig


class ResolverService(ResolverInterface):
    def __init__(self, config: HostsConfig) -> None:
        self.config: HostsConfig = config

    async def resolve(self: Self, service_name: str) -> str:
        host = vars(self.config)[service_name]
        return host
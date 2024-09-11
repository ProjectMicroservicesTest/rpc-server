from pydantic_settings import BaseSettings
from pydantic import Field


class RabbitConfig(BaseSettings): ...


class HostsConfig(BaseSettings): ...
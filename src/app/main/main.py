from faststream.asgi import AsgiFastStream

from src.app.infrastructure.brokers.rabbit_broker import rabbit_broker
from src.app.main.config import RabbitConfig
from src.app.presentation.web_rpc.v1.router import router


def get_faststream_app() -> AsgiFastStream:
    broker=rabbit_broker(config=RabbitConfig())
    broker.include_router(router)
    return AsgiFastStream(broker)

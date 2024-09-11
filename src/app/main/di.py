from src.app.application.usecases.requests_usecase import RequestUsecase
from src.app.infrastructure.services.request_service import RequestsService
from src.app.infrastructure.services.resolver_service import ResolverService
from src.app.main.config import HostsConfig

async def request_usecase() -> RequestUsecase:
    return RequestUsecase(
        request_interface=RequestsService(),
        resolver_interface=ResolverService(
            config=HostsConfig()
        )
    )
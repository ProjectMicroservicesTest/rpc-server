from typing import Self, Tuple

from src.app.application.contracts.requests_interface import RequestsInterface
from src.app.application.contracts.resolver_interface import ResolverInterface
from src.app.application.dto.request_dto import RequestDto
from src.app.domain.entities.request_entity import RequestEntity


class RequestUsecase:
    def __init__(
        self: Self, request_interface: RequestsInterface, resolver_interface: ResolverInterface
    ) -> None:
        self.request_interface: RequestsInterface = request_interface
        self.resolver_interface: ResolverInterface = resolver_interface

    async def make_request(self: Self, request: RequestDto) -> Tuple[dict, int]:
        if not request.headers:
            request.headers = {}
        if not request.data:
            request.data = {}

        host = await self.resolver_interface.resolve(
            request.path.split('/')[0]
        )
        url = f'http://{host}{request.path}'
        response, status_code = await self.request_interface.make_request(
            request=RequestEntity(
                method=request.method,
                url=url,
                headers=request.headers,
                data=request.data,
                params=request.params
            )
        )
        return response, status_code

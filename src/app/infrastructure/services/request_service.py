from typing import Self, Tuple

import aiohttp

from src.app.domain.entities.request_entity import RequestEntity
from src.app.application.contracts.requests_interface import RequestsInterface

class RequestsService(RequestsInterface):
    def __init__(self: Self) -> None:
        pass

    async def make_request(self: Self, request: RequestEntity) -> Tuple[dict, int]:
        print(request.url)
        async with aiohttp.ClientSession() as session:
            req=getattr(session, request.method)
            async with await req(
                request.url, params=request.params, json=request.data, headers=request.headers
            ) as response:
                response_json = await response.json()
                return response_json, response.status
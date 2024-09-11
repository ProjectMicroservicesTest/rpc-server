from typing import Annotated, Tuple

from faststream.rabbit.router import RabbitRouter
from faststream import Depends

from src.app.main.di import request_usecase
from src.app.presentation.shemas.request_shema import RequestShema
from src.app.application.usecases.requests_usecase import RequestUsecase
from src.app.application.dto.request_dto import RequestDto

router=RabbitRouter()


@router.subscriber('/make-request')
async def make_request(
    shema: RequestShema, request: Annotated[RequestUsecase, Depends(request_usecase)]
) -> Tuple[dict, int]:
    dto = RequestDto(
        params=shema.params,
        method=shema.method,
        headers=shema.headers,
        data=shema.data,
        path=shema.path
    )
    return await request.make_request(request=dto)

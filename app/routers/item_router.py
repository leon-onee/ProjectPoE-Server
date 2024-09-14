from fastapi import APIRouter, HTTPException, Response
from app.controllers.item_controller import process_items_from_url
from app.views.item_view import get_items_in_ndjson
from app.models.requests import POBUrlRequest

router = APIRouter()


@router.post("/items/")
async def fetch_items(request: POBUrlRequest):
    """Маршрут для получения всех предметов по URL и возврата их в формате NDJSON."""
    # return {"url": request}
    try:
        # Получаем все предметы через контроллер
        items = process_items_from_url(request.pob_url)

        # Преобразуем список предметов в формат NDJSON
        ndjson_result = get_items_in_ndjson(items)

        # Возвращаем результат с заголовком NDJSON
        return Response(content=ndjson_result, media_type="application/x-ndjson")

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

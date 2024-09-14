from fastapi import APIRouter, HTTPException
from app.controllers.build_controller import fetch_xml_from_url, fetch_xml_from_pobb
from app.views.build_view import get_xml_response

router = APIRouter()

@router.post("/fetch_xml/")
async def fetch_xml(url: str):
    """Маршрут для получения XML с pastebin.com."""
    try:
        xml_data = fetch_xml_from_url(url)
        return get_xml_response(xml_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/fetch_xml_pobb/")
async def fetch_xml_pobb(url: str):
    """Маршрут для получения XML с pobb.in."""
    try:
        xml_data = fetch_xml_from_pobb(url)
        return get_xml_response(xml_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

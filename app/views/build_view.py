from fastapi import APIRouter, HTTPException
from app.controllers.build_controller import BuildController

router = APIRouter()


@router.get("/fetch-xml/")
def fetch_xml(url: str):
    try:
        xml_data = BuildController.get_xml_from_url(url)
        return {"xml": xml_data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера")

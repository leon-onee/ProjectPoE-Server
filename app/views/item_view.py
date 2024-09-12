from fastapi import APIRouter, HTTPException
from app.controllers.item_controller import ItemController

router = APIRouter()

@router.post("/parse-item/")
def parse_item(text: str):
    try:
        item_info = ItemController.parse_item(text)
        return item_info
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

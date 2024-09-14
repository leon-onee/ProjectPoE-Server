import json
from fastapi import HTTPException


def get_items_in_ndjson(items: list) -> str:
    """Возвращает предметы в формате NDJSON."""
    try:
        ndjson_data = "\n".join([json.dumps(item) for item in items])
        return ndjson_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при создании NDJSON: {str(e)}")

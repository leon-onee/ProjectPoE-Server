from fastapi import HTTPException


def get_xml_response(xml_data: str) -> str:
    """Возвращает XML в виде строки."""
    if not xml_data:
        raise HTTPException(status_code=404, detail="XML не найден")

    return xml_data

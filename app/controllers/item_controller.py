from app.services.item_parser_service import ItemParserService


def process_items_from_url(url: str) -> list:
    """Контроллер для получения XML и парсинга всех предметов."""
    parser = ItemParserService()
    return parser.parse_items_from_xml(url)

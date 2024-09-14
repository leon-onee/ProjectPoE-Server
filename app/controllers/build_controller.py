from app.services.build_parser_service import BuildParser


def fetch_xml_from_url(url: str) -> str:
    """Контроллер для обработки URL и получения XML данных."""
    parser = BuildParser(url)
    return parser.fetch_xml_from_url()


def fetch_xml_from_pobb(url: str) -> str:
    """Контроллер для получения XML данных с pobb.in."""
    parser = BuildParser(url)
    return parser.get_xml_from_pobb()

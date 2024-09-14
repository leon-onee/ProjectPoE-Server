import xml.etree.ElementTree as ET
from app.services.build_parser_service import BuildParser
from app.models.item_model import ItemModel
from app.services.item_parser import ItemParser


class ItemParserService:
    def parse_items_from_xml(self, url: str) -> list:
        """Получение XML и парсинг всех предметов из него."""
        # Получаем XML с помощью BuildParser
        build_parser = BuildParser(url)
        # xml_data = build_parser.fetch_xml_from_url()
        xml_data = build_parser.get_xml_from_pobb()

        # Парсим XML для извлечения предметов
        root = ET.fromstring(xml_data)
        all_items = []

        for item in root.iter("Item"):
            # Получаем текст предмета и используем ItemParser для его парсинга
            item_text = item.text
            item_parser = ItemParser(item_text)

            # Создаем объект ItemModel с использованием данных из ItemParser
            parsed_item = ItemModel(
                name=item_parser.get_name(),
                rarity=item_parser.get_rarity(),
                crafted=item_parser.get_is_crafted() == "true",
                implicits=item_parser.get_implicits_stats(),
                stats=item_parser.get_stats()
            )

            # Добавляем полную информацию о предмете в список
            all_items.append(parsed_item.get_full_item_info())

        return all_items

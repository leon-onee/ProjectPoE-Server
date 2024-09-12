from app.models.item_model import ItemModel

class ItemController:
    @staticmethod
    def parse_item(raw_text: str):
        item = ItemModel(raw_text)
        return item.get_full_item_info()

from app.models.item_parser import ItemParser


class ItemModel:
    def __init__(self, raw_text: str):
        self.parser = ItemParser(raw_text)
        self.name = self.parser.get_name()
        self.rarity = self.parser.get_rarity()
        self.is_crafted = self.parser.get_is_crafted()
        self.implicits = self.parser.get_implicits_stats()
        self.stats = self.parser.get_stats()

    def get_full_item_info(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "is_crafted": self.is_crafted,
            "implicits": self.implicits,
            "stats": self.stats
        }


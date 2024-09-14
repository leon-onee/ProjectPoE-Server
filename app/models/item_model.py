from pydantic import BaseModel
from typing import List


class ItemModel(BaseModel):
    name: str
    rarity: str
    crafted: bool
    implicits: List[str]
    stats: List[str]

    def get_full_item_info(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "crafted": self.crafted,
            "implicits": self.implicits,
            "stats": self.stats
        }

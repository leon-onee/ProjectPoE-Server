import re


class ItemParser:
    def __init__(self, text: str):
        self.text = text.strip()
        self.arr = text.strip().split("\n")

    def get_rarity(self) -> str:
        pattern = 'Rarity:\s*(\w+)'
        match = re.search(pattern, self.text)

        return match.group(1) if match else 'Rarity not found'

    def get_name(self) -> str:
        item_name = [name.strip() for name in self.arr[1:3]]

        return " ".join(item_name)

    def get_is_crafted(self) -> str:
        pattern = 'Crafted:\s*(\w+)'
        match = re.search(pattern, self.text)

        return match.group(1) if match else 'false'

    def __get_implicits(self):
        pattern = 'Implicits:\s*(\w+)'
        match = re.search(pattern, self.text)

        return match

    def get_implicits_stats(self):
        match = self.__get_implicits()
        implicits_count = int(match.group(1))
        implicits_index = self.arr.index(match[0])

        return self.arr[implicits_index + 1:implicits_index + implicits_count + 1]

    def get_stats(self):
        match = self.__get_implicits()
        implicits_count = int(match.group(1))
        implicits_index = self.arr.index(match[0])
        stats_count = len(self.arr) - implicits_index - implicits_count - 1

        return self.arr[-stats_count:]
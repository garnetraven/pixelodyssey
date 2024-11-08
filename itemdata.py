from typing import Type
from entities.block import Block

class Item:
    def __init__(self, name: str = "default", quantity: int = 0) -> None:
        self.name = name
        self.quantity = quantity
        self.target_group = None

    def use(self, *args, **kwargs):
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Quantity: {self.quantity}"

class BlockItem(Item):
    def __init__(self, name: str, quantity: int = 1) -> None:
        super().__init__(name, quantity)

    def use(self, image, position, groups, chunk, *args, **kwargs):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0
        else:
            block = items[self.name].use_type(groups, image, position, name = self.name, hardness = items[self.name].hardness, durability = items[self.name].durability)
            chunk.add_block(block)

        if self.quantity == 0:
            self.name = "default"

class ItemData:
    def __init__(self, name: str, type: Type[Item], groups = ["sprites", "block_group"], use_type: Type[Block] = Block, type_str: str = "block", durability: int = 20, hardness: int = 1, strength: int = 1) -> None:
        self.name = name
        self.type = type
        self.type_str = type_str
        self.groups = groups
        self.use_type = use_type
        self.durability = durability
        self.hardness = hardness
        self.strength = strength

items = {
        "stone": ItemData("stone", BlockItem),
        "dirt": ItemData("dirt", BlockItem),
        "grass": ItemData("grass", BlockItem),
}

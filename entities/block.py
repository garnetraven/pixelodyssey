import pygame
from globals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple, name: str = "default", type = "block", durability: int = 20, hardness: int = 1):
        super().__init__(groups)
        self.name = name
        self.type = type
        self.in_groups = groups
        self.image = image.copy()
        self.rect = self.image.get_rect(bottomleft = (position[0], position[1] + TILESIZE))
        self.active = True
        self.hardness = hardness
        self.durability = durability

    def break_block(self, strength) -> bool:
        if strength >= self.hardness:
            self.durability -= 1 * strength
            if self.durability < 1:
                self.active = False
                self.kill()
                return True
        return False



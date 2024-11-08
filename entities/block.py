import pygame
from globals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, groups, image: pygame.Surface, position: tuple, name: str = "default", type = "block", durability: int = 20, hardness: int = 1):
        super().__init__(groups)
        self.name = name
        self.type = type
        self.in_groups = groups
        self.image = image.copy
        self.image = pygame.Surface((TILESIZE * 2,TILESIZE * 2))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()

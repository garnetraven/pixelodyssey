import pygame
from globals import *

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((TILESIZE * 2,TILESIZE * 3))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()

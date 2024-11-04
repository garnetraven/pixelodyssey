import pygame
from utils.state import State
from entities.player import Player

class OpenWorld(State):
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen

        self.player = Player()

        self.all_sprites = pygame.sprite.Group(self.player)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill('lightblue')
        self.all_sprites.draw(self.screen)


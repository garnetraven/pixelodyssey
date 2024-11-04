import pygame
from utils.state import State
from entities.player import Player

class OpenWorld(State):
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen

        self.player = Player()

        self.sprites = pygame.sprite.Group(self.player) 

    def update(self):
        self.sprites.update()

    def draw(self):
        self.screen.fill('lightblue')
        self.sprites.draw(self.screen)


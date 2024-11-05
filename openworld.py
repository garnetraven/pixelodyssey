import pygame
from opensimplex import OpenSimplex
from utils.state import State
from groups.camera import Camera
from entities.player import Player
from entities.block import Block
from utils.eventhandler import EventHandler
from globals import *

class OpenWorld(State):
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen

        self.sprites = Camera() 
        self.blocks = pygame.sprite.Group() 

        self.player = Player(self.blocks)

        self.sprites.add(self.player)

        self.gen_world()

    def gen_world(self):
        noise_generator = OpenSimplex(seed = 112340987613248) 
        width = 100
        height = 20
        x_offset = 50 * TILESIZE
        y_offset = 35

        for x in range(width):
            column = []
            for y in range(height):
                noise_value = noise_generator.noise2(x * 0.1, y * 0.1)
                height_value = int((noise_value + 1) / 2 * height + 10)
                column.append(height_value)

                if height_value > 0:
                    block = Block()
                    block.rect.x = x * TILESIZE - x_offset
                    block.rect.y = (height - height_value + y_offset) * TILESIZE
                    self.sprites.add(block)
                    self.blocks.add(block)

    def update(self):
        self.sprites.update()

        if EventHandler.keydown(pygame.K_p):
            self.app.active_state = "paused"


    def draw(self):
        self.screen.fill('lightblue')
        self.sprites.draw(self.screen, self.player)


import pygame
from opensimplex import OpenSimplex
from utils.state import State
from groups.camera import Camera
from entities.player import Player
from entities.block import Block
from utils.eventhandler import EventHandler
from inventory.inventory import Inventory
from texturedata import overworld_atlas
from globals import *
import random

class OpenWorld(State):
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen

        self.sprites = Camera() 
        self.blocks = pygame.sprite.Group() 

        self.inventory = Inventory(self.app)

        self.player = Player(self.blocks)

        self.sprites.add(self.player)

        self.textures = self.gen_textures(overworld_atlas, "res/overworld_atlas.png", (256, 256))

        self.gen_world()

    def gen_world(self):
        noise_generator = OpenSimplex(seed=112340987613248) 
        heightmap = []
        for x in range(300):
            noise_value = noise_generator.noise2(x * 0.05, 0)
            height = int((noise_value + 1) * 5 + 10)
            heightmap.append(height)

        for x in range(len(heightmap)):
            for y in range(heightmap[x]):
                block_position = (x * TILESIZE - (len(heightmap) / 2) * TILESIZE, 30 * TILESIZE - y * TILESIZE)
                block_type = "grass"
                if y < heightmap[x] - 1:
                    block_type = "dirt"
                if y < heightmap[x] - 5 + random.randint(-2, 2):
                    block_type = "stone"
                if block_type == 'stone' and random.randint(0,15) < 2:
                    block_type = 'coal_ore'

                Block([self.sprites, self.blocks], image=self.textures[block_type], position=block_position, name=block_type)

    def gen_textures(self, texturedata, file_path, size) -> dict:
        atlas_img = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(), size)

        textures = {}
        for name, data in texturedata.items():
            textures[name] = pygame.transform.scale(
                pygame.Surface.subsurface(atlas_img, pygame.Rect(
                    data.position[0] * TRUE_TILESIZE,
                    data.position[1] * TRUE_TILESIZE,
                    data.size[0],
                    data.size[1]
                )),
                (TILESIZE, TILESIZE)
            )
        return textures

    def update(self):
        self.sprites.update()
        self.inventory.update()

        if EventHandler.keydown(pygame.K_ESCAPE):
            self.app.active_state = "paused"


    def draw(self):
        self.screen.fill('lightblue')
        self.sprites.draw(self.screen, self.player)
        self.inventory.draw()


from globals import *

class Atlas:
    def __init__(self, file_path: str, size: tuple, textures: dict):
        self.file_path = file_path
        self.size = size
        self.textures = textures

class AtlasTexture:
    def __init__(self, name: str, position: tuple, size: tuple, type = "default") -> None:
        self.name = name
        self.position = position
        self.size = size
        self.type = type

class Texture:
    def __init__(self, name: str, size: tuple, file_path: str, type: str = "default") -> None:
        self.name = name
        self.size = size
        self.file_path = file_path
        self.type = type


overworld_atlas = {
    "stone": AtlasTexture("stone", (0, 0), (8, 8)), 
    "dirt": AtlasTexture("dirt", (1, 0), (8, 8)), 
    "grass": AtlasTexture("grass", (2, 0), (8, 8)), 
    "coal_ore": AtlasTexture("coal_ore", (3, 0), (8, 8)), 
    "gold_ore": AtlasTexture("gold_ore", (4, 0), (8, 8)), 
    "diamond_ore": AtlasTexture("diamond_ore", (5, 0), (8, 8)), 
    "iron_ore": AtlasTexture("iron_ore", (6, 0), (8, 8)), 
}

player_textures = {}

atlas_textures = {"overworld_atlas": Atlas("res/atlas/overworld_atlas.png", (256, 256), overworld_atlas)}

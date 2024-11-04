import pygame
from globals import *
from utils.state import State
from utils.eventhandler import EventHandler

class MainMenu(State):
    def __init__(self, app) -> None:
        MainMenu.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen

        # text
        self.title = "Pixel Odyssey"
        self.title_text = MainMenu.font.render(self.title, True, "black", None)
        self.title_rect = self.title_text.get_rect(center = (SCREENWIDTH // 2, SCREENHEIGHT // 2))


    def update(self) -> None:
        pass
    
    def draw(self) -> None:
        self.screen.fill("black")
        self.screen.blit(self.title_text, self.title_rect)

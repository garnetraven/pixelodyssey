import pygame
from globals import *
from utils.state import State
from ui.components import StateButton 

class Options(State):
    def __init__(self, app) -> None:
        Options.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen

        # text
        self.title = "Options"
        self.title_text = Options.font.render(self.title, True, "white", None)
        self.title_rect = self.title_text.get_rect(center = (SCREENWIDTH // 2, SCREENHEIGHT // 2))
        self.buttons = [
            StateButton(self.screen, "Back", "mainmenu", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50)),
        ]

    def update(self) -> None:
        for button in self.buttons:
            if button.clicked():
                button.use(self.app)
    
    def draw(self) -> None:
        self.screen.fill("black")
        for button in self.buttons:
            button.draw(self.screen)
        self.screen.blit(self.title_text, self.title_rect)

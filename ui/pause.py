import pygame
from globals import *
from utils.state import State
from ui.components import StateButton 
from utils.eventhandler import EventHandler

class Pause(State):
    def __init__(self, app) -> None:
        Pause.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen

        # text
        self.title = "Paused"
        self.title_text = Pause.font.render(self.title, True, "black", None)
        self.title_rect = self.title_text.get_rect(center = (SCREENWIDTH // 2, SCREENHEIGHT // 2))
        self.buttons = [
            StateButton(self.screen, "Resume", "open_world", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50)),
            StateButton(self.screen, "Options", "options", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 100)),
            StateButton(self.screen, "Main Menu", "mainmenu", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 150)),
        ]

    def update(self) -> None:
        if EventHandler.keydown(pygame.K_ESCAPE):
            self.app.active_state = "open_world"
        for button in self.buttons:
            if button.clicked():
                button.use(self.app)
    
    def draw(self) -> None:
        for button in self.buttons:
            button.draw(self.screen)
        self.screen.blit(self.title_text, self.title_rect)

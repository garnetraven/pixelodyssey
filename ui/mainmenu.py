import pygame
from globals import *
from utils.state import State
from ui.components import StateButton, QuitButton

class MainMenu(State):
    def __init__(self, app) -> None:
        MainMenu.font = pygame.font.Font(None, 45)

        self.app = app
        self.screen = self.app.screen

        # text
        self.title = "Pixel Odyssey"
        self.title_text = MainMenu.font.render(self.title, True, "white", None)
        self.title_rect = self.title_text.get_rect(center = (SCREENWIDTH // 2, SCREENHEIGHT // 2))
        self.buttons = [
            StateButton(self.screen, "Play", "open_world", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50)),
            StateButton(self.screen, "Options", "options", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 100)),
            QuitButton(self.screen, "Quit", (SCREENWIDTH // 2, SCREENHEIGHT // 2 + 150))
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

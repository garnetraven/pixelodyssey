import pygame
from utils.eventhandler import EventHandler

class Button:
    def __init__(self, screen, text: str, position: tuple) -> None:
        self.screen = screen
        self.text = pygame.font.Font(None, 45).render(text, True, "white")
        self.rect = self.text.get_rect(center = position)

    def clicked(self) -> bool:
        if EventHandler.clicked():
            mouse_pos = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_pos)

    def use(self, *args, **kwargs):
        pass

    def draw(self, display: pygame.Surface):
        display.blit(self.text, self.rect)

class StateButton(Button):
    def __init__(self, screen, text: str, state: str, position: tuple) -> None:
        super().__init__(screen, text, position)
        self.state = state

    def use(self, app):
        app.active_state = self.state

class QuitButton(Button):
    def __init__(self, screen, text: str, position: tuple) -> None:
        super().__init__(screen, text, position)

    def use(self, app):
        app.running = False

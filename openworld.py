from utils.state import State

class OpenWorld(State):
    def __init__(self, app):
        self.app = app
        self.screen = self.app.screen

    def update(self):
        pass

    def draw(self):
        self.screen.fill('lightblue')


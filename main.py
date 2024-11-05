import pygame
import sys
from globals import *
from utils.eventhandler import EventHandler
from ui.mainmenu import MainMenu
from ui.options import Options
from ui.pause import Pause
from openworld import OpenWorld

class Game:
    """
    Main game class that handles initialization, game loop, and state management.
    
    Attributes:
        screen (pygame.Surface): The main display surface.
        clock (pygame.time.Clock): Clock for controlling game's framerate.
        running (bool): Flag to control the game loop.
        states (dict): Dictionary of game states.
        active_state (str): Key of the currently active game state.
    """
    def __init__(self) -> None:
        """Initialize the game, setting up the display and game states."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

        self.clock = pygame.time.Clock()

        self.running = True

        # Initialize game states
        self.states ={
            'mainmenu': MainMenu(self),
            'open_world': OpenWorld(self),
            'options': Options(self),
            'paused': Pause(self)
        }
        self.active_state = 'mainmenu'

    def start(self) -> None:
        """Start the game loop and handle cleanup after the game ends."""
        self.loop()
        self.close()

    def loop(self) -> None:
        """ Main game loop."""
        while self.running:
            self.update()
            self.draw()

    def update(self) -> None:
        """Update game logic, handle events, and update the active state."""
        EventHandler.poll_events()

        # Check for quit events
        if EventHandler.is_closed_requested():
            self.running = False

        # Update the active state
        self.states[self.active_state].update()

    def draw(self) -> None:
        """Draw the current game state and update the display."""
        self.states[self.active_state].draw()
        pygame.display.flip()
        self.clock.tick(FPS)

    def close(self) -> None:
        """Clean up and exit the game."""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()

# Python Journey - Chapter 30
# Creating a Pygame Window and Responding to User Input for Alien Invasion project

import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # set the background color
    bg_color = ai_settings.bg_color

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

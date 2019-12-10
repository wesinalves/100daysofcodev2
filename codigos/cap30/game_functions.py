# Python Journey - Chapter 30
# Game functions for Alien Invasion

import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the right
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # Stop moving the ship to the right
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # Stop moving the ship to the right
                ship.moving_left = False
            
                    

def update_screen(settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

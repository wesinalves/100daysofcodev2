# Python Journey - Chapter 30
# Bullet class for Alien Invasion game

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's current position."""

        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
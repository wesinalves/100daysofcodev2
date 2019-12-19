# Python Journey - Chapter 30
# Game functions for Alien Invasion

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        fire_bullet(settings, screen, ship, bullets)        

def check_keyup_events(event, ship):
    """Respond to keyreleases."""
    if event.key == pygame.K_RIGHT:
        # Stop moving the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Stop moving the ship to the right
        ship.moving_left = False

def check_events(settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
            
                    

def update_screen(settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to the new screen."""
        
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared. 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
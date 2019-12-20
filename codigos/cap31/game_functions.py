# Python Journey - Chapter 30
# Game functions for Alien Invasion

import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    
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

def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    avaiable_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avaiable_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien_height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.

    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(settings, screen, aliens, alien_number, row_number)
# Python Journey - Chapter 32
# Statistics for Alien Invasion game

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, settings):
        """Initialize statistics."""
        self.ai_settings = settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = False
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

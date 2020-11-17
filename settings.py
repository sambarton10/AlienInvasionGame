""" Settings File"""

class Settings:
    """A class to store all setttings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
    
        # Ship settings
        self.ship_speed = 3
        
        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 7
        self.bullet_height = 18
        self.bullet_color = (60,60,60)
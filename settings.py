import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (1, 0, 0)
        self.image = pygame.image.load('images/sky.bmp')

        # Ship settings
        self.ship_limit = 3

        self.ship_width = 33
        self.ship_height = 87
        self.ship_image = pygame.image.load('images/ship_1.bmp')

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (68, 55, 39)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_width = 60
        self.alien_height = 40
        self.fleet_drop_speed = 10

        self.alien_image = pygame.image.load('images/alien.bmp')

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction od 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *=self.speedup_scale
        self.bullet_speed *=self.speedup_scale
        self.alien_speed *=self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

import pygame

from Weapons_package.bullet_type_weapon_package.bullet_type_gun import Bullet_type_weapon

from Constants_package.constants import SCALE


# Define the Minigun class
class Minigun(Bullet_type_weapon):
    def __init__(self, center, damage_multiplier, fire_rate_multiplier):
        super().__init__(center, damage_multiplier, fire_rate_multiplier)

        # Stats
        self.damage = 12 * damage_multiplier
        self.fire_rate = 350 * fire_rate_multiplier
        self.bullet_speed = 20 * SCALE

        # Image data
        self.width = 7 * SCALE
        self.height = 7 * SCALE
        self.color = '#FBFBD1'

        # Image
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Position
        self.rect.center = center

        # Audio
        self.audio = pygame.mixer.Sound("Audio/minigun.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()
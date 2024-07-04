import pygame
import random


from Enemies_package.enemy import Enemy
from Enemies_package.Enemy_gun_package.enemy_gun import Enemy_gun

from Constants_package.constants import players, enemies_laser_guns, SCREEN_WIDTH, SCALE, fullscreen_flag


# Define the Star_lord class
class Star_lord(Enemy):
    def __init__(self):
        super().__init__()

        # Stats
        self.hp = 120
        self.speed_x = 3 * SCALE
        self.speed_y = 5 * SCALE
        self.acceleration = 1
        self.damage = 1

        # Timer
        self.star_lord_timer = 0


        # Image
        self.image = pygame.image.load('Graphics/star_lord.png').convert_alpha()
        if fullscreen_flag:
            self.image = pygame.transform.scale(self.image, (136, 104))
        else:
            self.image = pygame.transform.scale(self.image, (106, 80))
        self.rect = self.image.get_rect()

        # Position
        self.rect.x = random.randrange(100 * SCALE, SCREEN_WIDTH - 100 * SCALE)
        self.rect.y = 100 * SCALE

        # Audio
        self.audio = pygame.mixer.Sound("Audio/star_lord.mp3")
        self.audio.set_volume(0.5)
        self.audio.play()

    def movement_service(self):
        self.rect.x += self.speed_x * self.acceleration
        self.rect.y += self.speed_y
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.bottom >= 300 * SCALE:
            self.speed_y = self.speed_y * -1

        if self.rect.top <= 0:
            self.speed_y = self.speed_y * -1

        if self.rect.centery <= 150:
            self.acceleration = 5
        else:
            self.acceleration = 1

    def melee_attack_service(self):
        collided_player = pygame.sprite.spritecollide(self, players, False)

        if collided_player:
            for player in collided_player:
                player.hp += -self.damage
                if player.hp <= 0:
                    player.kill()

    def range_attack_service(self):
        if self.star_lord_timer <= 0:
            enemy_laser_gun = Enemy_gun(self.rect.center, 1.5, 2500, 10, 25, 45, 'Graphics/laserRed.png')
            enemies_laser_guns.add(enemy_laser_gun)
            self.star_lord_timer = enemy_laser_gun.fire_rate
        self.star_lord_timer += -100



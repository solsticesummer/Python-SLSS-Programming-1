# Pygame Drawing
# Author: Henry
# 14 January 2026

import random

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/mario copy.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100

    def calc_damage(self, amt: int) -> int:
        """Decease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health


class Lazer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/lazer.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = 300
        self.rect.centery = 300

    def update(self):
        # movement in the x-axis
        self.rect.x += self.vel_x
        # movement in the y-axis
        self.rect.y += self.vel_y


class Light(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/light.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = 300
        self.rect.centery = 300

    def update(self):
        # movement in the x-axis
        self.rect.x += self.vel_x
        # movement in the y-axis
        self.rect.y += self.vel_y


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)
    TITLE = "LAZER"

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)

    # Variables
    done = False
    clock = pygame.time.Clock()
    score = 0
    num_enemies = 10

    # Sprites groups
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    all_group = pygame.sprite.Group()

    for _ in range(num_enemies):
        enemy = Lazer()
        enemy.vel_x = random.randint(-5, 5)
        enemy.vel_y = random.randint(-5, 5)
        all_group.add(enemy)
        enemy_group.add(enemy)

    mario = Player()
    all_group.add(mario)
    player_group.add(mario)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        enemy_collided = pygame.sprite.spritecollide(mario, enemy_group, False)
        for enemy in enemy_collided:
            print(f"Health: {mario.calc_damage(10)}")

        for enemy in enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1

        # ------ DRAWING TO SCREEN
        screen.fill(BLACK)
        all_group.draw(screen)
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()

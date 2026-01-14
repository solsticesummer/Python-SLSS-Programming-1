# Pygame Drawing
# Author: Henry
# 14 January 2026

import random

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100


class Lazer(pygame.sprite.Sprite):
    def __init(self):
        super().__init__()

        self.image = pygame.image.load("assets/lazer.png")
        self.rect = self.image.get_rect()


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

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        lazer_collided = pygame.sprite.Spritecollide(Player, Lazer, True)
        if lazer_collided:
            print(f"Score: {player.calc_damage}")
        # ------ DRAWING TO SCREEN
        screen.fill(BLACK)
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()

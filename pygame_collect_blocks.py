# Pygame Collect Blocks
# Author: Henry
# Date: 7 Jan 2026

import random

import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, color: pygame.Color, width: int, height: int):
        """A block of any color"""
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # A Rect tells you two things:
        # - How big the htibox is (width, height)
        # - Where it is on the screen (x, y)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """A Mario character"""
        super().__init__()

        self.image = pygame.image.load("mario.png")
        self.rect = self.image.get_rect()

    def update(self):
        """Update Mario's location based on mouse pos"""
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos


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

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # Create a Sprite Group
    all_sprites_group = pygame.sprite.Group()

    # Create Mario
    player = Mario()
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    all_sprites_group.add(player)

    # Create 100 Blocks
    for i in range(0, 100):
        block = Block(BLUE, 20, 10)
        block.rect.centerx = random.randint(0, WIDTH)
        block.rect.centery = random.randint(0, HEIGHT)
        all_sprites_group.add(block)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites_group.draw(screen)
        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()

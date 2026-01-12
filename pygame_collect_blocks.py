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

        self.image_right = pygame.image.load("Assets/mario.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0
        self.health = 100

    def calc_damage(self, amt: int) -> int:
        """Decease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health

    def update(self):
        """Update Mario's location based on mouse pos"""

        self.rect.center = pygame.mouse.get_pos()

        # If Mario's previous x is less than current x
        #   Then Mario is facing Right
        # If Mario's previous x is greater than current x
        #   Then Mario is facing left
        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/goomba.png")
        self.rect = self.image.get_rect()

        self.vel_x = 1
        self.vel_y = 1

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

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()
    score = 0
    num_enemies = 5

    # Create a Sprite Group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    for _ in range(num_enemies):
        enemy = Enemy()
        enemy.vel_x = random.randint(-5, 5)
        enemy.vel_y = random.randint(-5, 5)
        enemy.rect.center = (WIDTH / 2, HEIGHT / 2)
        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    # Create Mario
    player = Mario()
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    all_sprites_group.add(player)

    # Create 100 Blocks
    # Randomly place them throughout the screen
    for i in range(0, 100):
        block = Block(BLUE, 20, 10)
        block.rect.centerx = random.randint(0, WIDTH)
        block.rect.centery = random.randint(0, HEIGHT)
        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep enemies in screen
        # Bounce off the right side
        for enemy in enemy_sprites_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1

        # TODO: Check if Mario collides with a block
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        if blocks_collided:
            print("-----")
            print("Mario collected a block!")
            score += 1
            print(score)

        # TODO: Collision between Player and Enemies
        enemies_collided = pygame.sprite.spritecollide(
            player, enemy_sprites_group, False
        )
        for enemy in enemies_collided:
            # Decrease mario's life
            print(player.calc_damage(10))

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

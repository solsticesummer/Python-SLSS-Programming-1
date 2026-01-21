# Pygame Drawing
# Author: Henry
# 14 January 2026

import random

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1000
        self.image_right = pygame.image.load("assets/mario copy.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        self.vel_x = 0
        self.vel_y = 0

        self.previous_x = 0

    def calc_damage(self, amt: int) -> int:
        """Decease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health

    def move_up(self):
        self.vel_y -= 10

    def move_down(self):
        self.vel_y += 10

    def move_left(self):
        self.vel_x -= 10

    def move_right(self):
        self.vel_x += 10

    def stop(self):
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        # movement in the x-axis
        self.rect.x += self.vel_x
        # movement in the y-axis
        self.rect.y += self.vel_y

        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Lazer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/lazer.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(0, 800)
        self.rect.centery = random.randint(0, 600)

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
    level = 1
    score = 0
    num_enemies = 5
    main_font = pygame.font.SysFont("Arial", 50)

    # Sprites groups
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    all_group = pygame.sprite.Group()

    mario = Player()
    all_group.add(mario)
    player_group.add(mario)

    for _ in range(num_enemies):
        enemy = Lazer()
        enemy.vel_x = random.randint(-2, 2)
        enemy.vel_y = random.randint(-2, 2)
        if enemy.vel_x == 0:
            enemy.vel_x = 1
        if enemy.vel_y == 0:
            enemy.vel_y = 1
        all_group.add(enemy)
        enemy_group.add(enemy)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # TODO: If the user presses W, then move mario up
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    mario.move_up()
                if event.key == pygame.K_a:
                    mario.move_left()
                if event.key == pygame.K_s:
                    mario.move_down()
                if event.key == pygame.K_d:
                    mario.move_right()
            if event.type == pygame.KEYUP:
                mario.stop()
        # ------ GAME LOGIC
        score += 1
        if score % 1000 == 0:
            level += 1
            # Increase the speed of enemies and mario
            for enemy in enemy_group:
                enemy.vel_x *= 2
                enemy.vel_y *= 2

        all_group.update()
        enemy_collided = pygame.sprite.spritecollide(mario, enemy_group, False)
        for enemy in enemy_collided:
            print(f"Health: {mario.calc_damage(10)}")

        for enemy in enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x *= -1
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y *= -1

        if mario.rect.left < 0 or mario.rect.right > WIDTH:
            mario.vel_x *= -1
        if mario.rect.top < 0 or mario.rect.bottom > HEIGHT:
            mario.vel_y *= -1
        if mario.health <= 0:
            print("Game Over")
            print("Final Score:", score)
            done = True

        # ------ DRAWING TO SCREEN
        screen.fill(BLACK)
        all_group.draw(screen)

        score_text = main_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 2))

        level_text = main_font.render(f"Level: {level}", True, WHITE)
        screen.blit(level_text, (400, 2))

        # Draw health bar
        health_bar_width = mario.health / WIDTH
        pygame.draw.rect(screen, GREEN, (10, 50, health_bar_width * 400, 20))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()

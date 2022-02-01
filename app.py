# Balloon Shooting Challenge
# -----------------------------------------------------------------------------------------
#
# RULES #
#   Goal is to shoot the balloon down
#   Player can move the cannon up and down using the arrow keys
#   Fire a bullet by pressing the space key
#   Balloon moves up and down randomly
#   Player can shoot one or multiple bullets at a time
#   Game is over when the balloon is shot
#
#   ---------------------------------------------------------------------------------------

# TO DO
# Cannon movement
# Balloon movement
# Bullet movement
# Detecting collision
# Updating the number of misses
# Handling end of game

import pygame
import os
from random import seed, randint
from time import time


# defines
WIDTH, HEIGHT = 827, 570
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
PLAYER_VEL = 5

RANDOM_CHANCE = 5
FRAMES = 25

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
ENEMY_WIDTH, ENEMY_HEIGHT = 80, 80


all_sprites = pygame.sprite.Group()
balloongroup = pygame.sprite.Group()
seed(time())


def random_start_direction():
    if randint(0, 1):
        return 1
    else:
        return -1

# set up assets
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (827, 570))

PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'pea_shooter.png'))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

ENEMY_IMAGE = pygame.image.load(os.path.join('assets', 'pokeball.png'))
ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_WIDTH, ENEMY_HEIGHT))


# initialise screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokeball Shooter")


def draw_screen(player):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(PLAYER_IMAGE, (player.x, player.y))
    pygame.display.update()


def handle_player_movement(press_keys, player):
    if press_keys[pygame.K_UP] and player.y - PLAYER_VEL > 0: # UP
        player.y -= PLAYER_VEL
    if press_keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height < HEIGHT - 40: # DOWN
        player.y += PLAYER_VEL


class Balloon(pygame.sprite.Sprite):
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        image = ENEMY_IMAGE
        self.image = image
        self.rect = image.get_rect()
        self.area = screen.get_rect()
        self.vector = vector
        self.move_count = 0
        self.rect.midright = self.area.midright

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle

        self.vector = (angle,z)
        self.move_count += 1

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        if self.move_count >= FRAMES:
            if self.random_direction():
                self.vector = (-angle, z)
            self.move_count = 0
        (dx, dy) = (z * 0, z * angle)
        return rect.move(dx, dy)

    def random_direction(self):
        if randint(0, RANDOM_CHANCE) == 0:
            return True


# main game loop
def main():

    # Set the game speed and random generator
    speed = 2
    seed(time())

    # Initialise player and enemy
    player = pygame.Rect(20, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    balloon = Balloon((random_start_direction(), speed))

    all_sprites.add(balloon)
    balloongroup.add(balloon)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(BACKGROUND, balloon.rect, balloon.rect)
        all_sprites.update()

        press_keys = pygame.key.get_pressed()
        handle_player_movement(press_keys, player)
        
        draw_screen(player)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
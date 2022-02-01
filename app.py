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

import pygame, random
import os
from time import time
from random import randint, uniform
vec = pg.math.Vector2


# defines
WIDTH, HEIGHT = 827, 570
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
PLAYER_VEL = 5
BALLOON_VEL = 2

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
BALLOON_WIDTH, BALLOON_HEIGHT = 80, 80


# set up assets
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (827, 570))

PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'pea_shooter.png'))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

BALLOON_IMAGE = pygame.image.load(os.path.join('assets', 'pokeball.png'))
BALLOON_IMAGE = pygame.transform.scale(BALLOON_IMAGE, (BALLOON_WIDTH, BALLOON_HEIGHT))

# balloon properties
MAX_SPEED = 5


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


# testing enemy movement
class Balloon(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        image = BALLOON_IMAGE
        self.image = image
        self.rect = image.get_rect()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.pos = vec(randint(0, WIDTH), randint(0, HEIGHT))
        self.vel = vec(MAX_SPEED, 0).rotate(uniform(0, 360))
        self.acc = vec(0, 0)
        self.rect.center = self.pos

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)


# main game loop
def main():
    player = pygame.Rect(20, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    balloon = balloon()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        press_keys = pygame.key.get_pressed()
        handle_player_movement(press_keys, player)
        draw_screen(player)

    pygame.quit()


if __name__ == "__main__":
    main()
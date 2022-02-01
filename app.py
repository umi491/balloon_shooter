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


# defines
WIDTH, HEIGHT = 827, 570
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
PLAYER_VEL = 5
ENEMY_VEL = 2

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
ENEMY_WIDTH, ENEMY_HEIGHT = 80, 80


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


def draw_screen(player, enemy):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(PLAYER_IMAGE, (player.x, player.y))
    screen.blit(ENEMY_IMAGE, (enemy.x, enemy.y))
    pygame.display.update()


def handle_player_movement(press_keys, player):
    if press_keys[pygame.K_UP] and player.y - PLAYER_VEL > 0: # UP
        player.y -= PLAYER_VEL
    if press_keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height < HEIGHT - 40: # DOWN
        player.y += PLAYER_VEL


# testing enemy movement
def handle_enemy_movement(enemy):
    
    if enemy.y - ENEMY_VEL > 0:
        enemy.y -= ENEMY_VEL


# main game loop
def main():
    player = pygame.Rect(20, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy = pygame.Rect(620, 425, ENEMY_WIDTH, ENEMY_HEIGHT)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        press_keys = pygame.key.get_pressed()
        handle_player_movement(press_keys, player)
        handle_enemy_movement(enemy)
        
        draw_screen(player, enemy)

    pygame.quit()


if __name__ == "__main__":
    main()
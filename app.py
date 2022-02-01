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

from tkinter.tix import BALLOON
import pygame
import os
from random import randint


# Defines
WIDTH, HEIGHT = 827, 570
FPS = 60
PLAYER_VEL = 5
BALLOON_VEL = 2
BULLET_VEL = 20
RANDOM_VAL = 25

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100
BALLOON_WIDTH, BALLOON_HEIGHT = 80, 80

BALLOON_HIT = pygame.USEREVENT
WHITE = (255, 255, 255)

# Background
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (827, 570))

# Player
PLAYER_IMAGE = pygame.image.load(os.path.join('assets', 'pea_shooter.png'))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Balloon
BALLOON_IMAGE = pygame.image.load(os.path.join('assets', 'pokeball.png'))
BALLOON_IMAGE = pygame.transform.scale(BALLOON_IMAGE, (BALLOON_WIDTH, BALLOON_HEIGHT))

# Initialise screen
pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokeball Shooter")

# Generates a random number between 0 - 5 inclusive for balloon movement
def randomiser():
    if randint(0, 5) == 0:
        return True

def draw_screen(player, balloon, store_bullets):
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(PLAYER_IMAGE, (player.x, player.y))
    balloon.draw()
    balloon.update()

    for bullet in store_bullets:
        pygame.draw.rect(SCREEN, WHITE, bullet)

class Balloon(pygame.sprite.Sprite):
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        image = BALLOON_IMAGE
        self.image = image
        self.rect = image.get_rect()
        self.area = SCREEN.get_rect()
        self.vector = vector
        self.count = 0
        self.rect.midright = (600, 100)

    def draw(self):
        SCREEN.blit(self.image, (self.rect.midright, self.rect.midright))

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            angle = -angle

        self.count += 1
        self.vector = (angle,z)

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        if self.count >= RANDOM_VAL:
            if randomiser():
                self.vector = (-angle, z)
            self.count = 0
        (dx, dy) = (z * 0, z * angle)
        return rect.move(dx, dy)

def handle_player_movement(press_keys, player):
    if press_keys[pygame.K_UP] and player.y - PLAYER_VEL > 0: # UP
        player.y -= PLAYER_VEL
    if press_keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height < HEIGHT - 40: # DOWN
        player.y += PLAYER_VEL

def handle_bullets(store_bullets, player, balloon):
    for bullet in store_bullets:
        bullet.x += BULLET_VEL
        if balloon.rect.left == bullet.right:
            pygame.event.post(pygame.event.Event(BALLOON_HIT))
            store_bullets.remove(bullet)

# Main game loop
def main():

    # Initialise player and balloon
    player = pygame.Rect(20, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    balloon = Balloon((1, BALLOON_VEL))

    store_bullets = []
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.x + player.width, player.y + player.height//2 - 2, 10, 5)
                    store_bullets.append(bullet)
        
        # Player movement
        press_keys = pygame.key.get_pressed()
        handle_player_movement(press_keys, player)

        handle_bullets(store_bullets, player, balloon)
        
        # Display assets on screen
        draw_screen(player, balloon, store_bullets)
        pygame.display.flip()
        
    pygame.quit()


if __name__ == "__main__":
    main()
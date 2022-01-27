# Balloon shooting challenge
# -----------------------------------------------------------------------------------------
#
# RULES
#   Goal is to shoot the balloon down
#   Player can move the cannon up and down using the arrow keys
#   Fire a bullet by pressing the space key
#   Balloon moves up and down randomly
#   Player can shoot one or multiple bullets at the same time
#   Game over when the balloon is shot
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


# defines
WIDTH, HEIGHT = 827, 570
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60


# load and modify assets
BACKGROUND = pygame.image.load(os.path.join('assets', 'background.jpg'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (827, 570))
PLAYER = pygame.image.load(
    os.path.join('assets', 'pea_shooter.png'))
PLAYER = pygame.transform.scale(PLAYER, (100, 100))


# initialise screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Shooter")

# paint on screen
def draw_screen():
    screen.fill(BLACK)
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(PLAYER, (20, 400))
    pygame.display.update()


# main game loop
def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
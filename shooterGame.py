import pygame
pygame.init()
from player import Soldier

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(800 * 0.8)


player = Soldier(200,200,3)
player2 = Soldier(400,200,3)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ShooterGame")

run=True
while run:
    screen.blit(player.image,player.rect)
    screen.blit(player2.image,player2.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
"""make a pygame.group for payer and use it in the blit function."""




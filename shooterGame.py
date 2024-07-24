import pygame
pygame.init()
from player import Soldier

player = Soldier(200,200,3)
player2 = Soldier(400,200,3)
player_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(player2)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(800 * 0.8)
class ShooterGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("ShooterGame")

    def run_game(self):
        run=True        
        while run:
            for entity in player_group:
                self.screen.blit(entity.image,entity.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
            
        pygame.quit()
"""make a pygame.group for payer and use it in the blit function."""

if __name__ == '__main__':
    sg = ShooterGame()
    sg.run_game()


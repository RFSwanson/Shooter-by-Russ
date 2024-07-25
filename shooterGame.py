import pygame
pygame.init()
from player import Soldier

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(800 * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ShooterGame")

#load images
img = pygame.image.load('img/background/sky_cloud.png')
bg_image = pygame.transform.scale(img,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_rect = bg_image.get_rect()
clock = pygame.time.Clock()
FPS = 60


class ShooterGame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player = Soldier(self,200,200,3)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.moving_left = False
        self.moving_right = False
        

    def run_game(self):
        run=True        
        while run:
            clock.tick(FPS)
            screen.blit(bg_image,bg_rect)
            self.player.move()
            for entity in self.player_group:
                screen.blit(entity.image,entity.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.moving_left = False

            pygame.display.update()
        
         
            
        pygame.quit()

if __name__ == '__main__':
    sg = ShooterGame()
    sg.run_game()


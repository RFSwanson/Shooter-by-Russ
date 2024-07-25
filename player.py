import pygame

#define player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self,sg,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        self.sg = sg
        img = pygame.image.load("img/player/Idle/0.png")
        self.image = pygame.transform.scale(img,(int(img.get_width()) * scale,int(img.get_height())* scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 1

    def move(self):
        if self.sg.moving_left == True:
            self.rect.x -= self.speed
        elif self.sg.moving_right == True:
            self.rect.x += self.speed

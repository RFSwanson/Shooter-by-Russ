import pygame

#define player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self,sg,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.sg = sg
        img = pygame.image.load("img/player/Idle/0.png")
        self.image = pygame.transform.scale(img,(int(img.get_width()) * scale,int(img.get_height())* scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def move(self):
        dx = 0
        dy = 0
        dx = self.speed

        if self.sg.moving_left == True:
            self.rect.x -= dx
            self.flip = True
            self.direction = -1
        elif self.sg.moving_right == True:
            self.rect.x += dx
            self.flip = False
            self.direction = 1

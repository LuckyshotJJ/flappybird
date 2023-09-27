
import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, img, location):
        super().__init__()
        self.location = location
        self.speedx = 4
        self.bird_pass = False
        self.image = img                           #一定要image
        self.rect = self.image.get_rect()          #一定要rect 設定位置
        if location == "bottom":
            self.rect.bottomleft = (x,y)
        elif location == "top":
            self.rect.topleft = (x,y)
    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.kill() #刪除物件
    def restart(self):
        self.kill()






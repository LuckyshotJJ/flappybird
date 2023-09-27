import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, imgs):
        super().__init__()
        self.imgs = imgs
        self.img_index = 0
        self.image = self.imgs[self.img_index]              #一定要image
        self.rect = self.image.get_rect()                   #一定要rect 設定位置
        self.rect.center = (x, y)                           #以哪個位置為基準 中心點(center) 右上(topright) 上(top)
        self.rect.bottom = y
        self.last_pic_time = pygame.time.get_ticks()        #經過時間
        self.img_frequency = 200                           #毫秒
        self.speed_y = 0                                    #鳥下落速度
        self.fly = True
    def update(self, ground_y):
        #飛翔動畫
        if self.fly:
            now = pygame.time.get_ticks()
            if now - self.last_pic_time > self.img_frequency:   #現在的時間-上次切換圖片時間 > 切換延遲時間
                self.img_index += 1
                if self.img_index >= len(self.imgs):            #只有3張圖大於之後變為0
                    self.img_index = 0
                self.image = pygame.transform.rotate(self.imgs[self.img_index], -self.speed_y * 2)         #設定成下一張圖片
                self.last_pic_time = now
        #引力
        self.speed_y += 0.5
        self.rect.y += self.speed_y
        if self.rect.bottom > ground_y:
            self.rect.bottom = ground_y

    def jump(self):
        self.speed_y = -10

    def game_over(self):
        self.fly = False
        self.image = pygame.transform.rotate(self.imgs[self.img_index], -90)
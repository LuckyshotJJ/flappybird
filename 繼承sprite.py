import pygame
import random
from bird import Bird
from pipe import Pipe

BLACK = (0, 0, 0)
SCREEN_WITDH = 780
SCREEN_HEIGHT = 600 
FPS = 60

pygame.init()

def generate_pipes(last_pipe_time, pipe_frequency, pipe_sprite):
    now = pygame.time.get_ticks()
    if now - last_pipe_time > pipe_frequency:
        random_height = random.randint(-100, 100)
        pipe_plus = Pipe(SCREEN_WITDH, SCREEN_HEIGHT / 2 + random_height + pipe_gap, pipe_img, "top")
        flip_pipe_img = pygame.transform.flip(pipe_img, False, True)
        pipe_minus = Pipe(SCREEN_WITDH, SCREEN_HEIGHT / 2 + random_height - pipe_gap, flip_pipe_img, "bottom")
        pipe_sprite.add(pipe_plus)
        pipe_sprite.add(pipe_minus)
        return now
    return last_pipe_time

#圖片讀取
bg_img = pygame.image.load("img/bg.png")                #圖片讀取
bg_img = pygame.transform.scale(bg_img, (780, 600))     #調整圖片大小
ground_img = pygame.image.load("img/ground.png")
pipe_img = pygame.image.load("img/pipe.png")
bird_imgs = []
for i in range(1, 3):
    bird_imgs.append(pygame.image.load(f"img/bird{i}.png"))

window = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")
pygame.display.set_icon(bird_imgs[0])

clock = pygame.time.Clock()

#地板
ground_speed = 4
ground_x = 0

#鳥
bird = Bird(200, 400, bird_imgs)
bird_sprite = pygame.sprite.Group()         #群組物件
bird_sprite.add(bird)                       #加入群組

#管子
pipe_gap = 75
pipe_sprite = pygame.sprite.Group()
pipe_frequency = 1500                       #管子刷新時間
last_pipe_time = pygame.time.get_ticks() - pipe_frequency

run = True
while run:
    clock.tick(FPS)
    #輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #更新
    ground_x -= ground_speed
    if ground_x < -100:       #讓地板看起來有再跑
        ground_x = 0
    bird_sprite.update() #呼叫這個群組裡面所有update方法
    pipe_sprite.update()
    last_pipe_time = generate_pipes(last_pipe_time, pipe_frequency, pipe_sprite)
    
    #顯示
    window.blit(bg_img, (0,0))  #畫圖 blit有順序關係 先畫鳥在畫背景背景會覆蓋鳥
    bird_sprite.draw(window)
    pipe_sprite.draw(window)
    window.blit(ground_img, (ground_x, SCREEN_HEIGHT - 100))
    pygame.display.update()


pygame.quit()
import pygame

BLACK = (0, 0, 0)
SCREEN_WITDH = 780
SCREEN_HEIGHT = 600 
FPS = 60

pygame.init()
window = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")

clock = pygame.time.Clock()

bg_img = pygame.image.load("img/bg.png")                #圖片讀取
bg_img = pygame.transform.scale(bg_img, (780, 600))     #調整圖片大小
bird_img = pygame.image.load("img/bird1.png")           #圖片讀取
ground_img = pygame.image.load("img/ground.png")
pipe_img = pygame.image.load("img/pipe.png")

pygame.display.set_icon(bird_img)
# bird_img = pygame.transform.rotate(bird_img, 60)        #旋轉逆時鐘
# bird_img = pygame.transform.flip(bird_img, True, False) #水平翻轉(bird_img, 要不要做水平翻轉, 要不要做垂直翻轉)

run = True
ground_speed = 4
ground_x = 0
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
    #顯示
    
    window.blit(bg_img, (0,0))  #畫圖 blit有順序關係 先畫鳥在畫背景背景會覆蓋鳥
    window.blit(bird_img, (100,150))
    window.blit(ground_img, (ground_x, SCREEN_HEIGHT - 100))
    pygame.display.update()
pygame.quit()
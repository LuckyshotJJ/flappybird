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
def restart(game_over):
    game_over = False
    for i in range(len(pipe_group.sprites())):
        pipe_group.sprites()[0].kill()
    bird_group.sprites()[0].rect.y = 100
    bird.speed_y = 0
    bird.fly = True
    return game_over
        
    
    
#圖片讀取
bg_img = pygame.image.load("img/bg.png")                #圖片讀取
bg_img = pygame.transform.scale(bg_img, (780, 600))     #調整圖片大小
ground_img = pygame.image.load("img/ground.png")
pipe_img = pygame.image.load("img/pipe.png")
restart_img = pygame.image.load("img/restart.png")

bird_imgs = []
for i in range(1, 3):
    bird_imgs.append(pygame.image.load(f"img/bird{i}.png"))

window = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
pygame.display.set_caption("flappy bird")
pygame.display.set_icon(bird_imgs[0])

#地板
ground_speed = 4
ground_x = 0
ground_y = SCREEN_HEIGHT - 100
#鳥
bird_y = 400
bird = Bird(200, 300, bird_imgs)
bird_group = pygame.sprite.Group()         #群組物件
bird_group.add(bird)                       #加入群組
#管子
pipe_gap = 75
pipe_group = pygame.sprite.Group()          #右鍵 重新命名符號可以改全部變數
pipe_frequency = 1500                       #管子刷新時間
last_pipe_time = pygame.time.get_ticks() - pipe_frequency
#分數
score_font = pygame.font.Font("微軟正黑體.ttf", 50)
score = 0
score_text = score_font.render(f"{score}", True, (255, 255, 255))

clock = pygame.time.Clock()
run = True
game_over = False

while run:
    clock.tick(FPS)
    #輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE  and game_over == True:
                game_over = restart(game_over)
                score = 0
                score_text = score_font.render(f"{score}", True, (255, 255, 255))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not game_over:
                bird.jump()
        
    #更新
    
    #碰撞判斷
    #(bird_sprite, pipe_sprite, True, False)碰撞到了bird_sprite要刪掉
    bird_group.update(ground_y) #呼叫這個群組裡面所有update方法  
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or bird.rect.bottom >= ground_y or bird.rect.top <= 0:
        game_over = True  
        bird.game_over()
    if not game_over:
        pipe_group.update()
        last_pipe_time = generate_pipes(last_pipe_time, pipe_frequency, pipe_group)
        #判斷通過管子
        try:
            first_pipe = pipe_group.sprites()[0]#遊戲群組裡物件
            if not first_pipe.bird_pass:
                if first_pipe.rect.right < bird.rect.left:          
                    score += 1
                    first_pipe.bird_pass = True
                    score_text = score_font.render(f"{score}", True, (255, 255, 255))
        except:
            pass
        ground_x -= ground_speed
        if ground_x < -100:       #讓地板看起來有再跑
            ground_x = 0
    #顯示
      #畫圖 blit有順序關係 先畫鳥在畫背景背景會覆蓋鳥
    
    window.blit(bg_img, (0,0))
    bird_group.draw(window)
    pipe_group.draw(window)
    window.blit(score_text, (SCREEN_WITDH / 2 - score_text.get_width()/ 2, 30))
    window.blit(ground_img, (ground_x, ground_y))
    if game_over:
        window.blit(restart_img, (SCREEN_WITDH / 2 - restart_img.get_width() / 2 , SCREEN_HEIGHT / 2 - restart_img.get_height() / 2))
    pygame.display.update()


pygame.quit()
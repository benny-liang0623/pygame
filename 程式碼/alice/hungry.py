
import pygame
from pygame import key
FPS=60 #每秒迴圈運轉次數

WIDTH=350
HEIGHT=350
g=(0,255,0)
#遊戲初始畫面
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
maze=pygame.image.load('C://Users//user//Desktop//maze.jpg')
pygame.display.set_caption("HungryAlice")
clock=pygame.time.Clock()
#sprite-代表遊戲內建的東西

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,10))
        self.image.fill(g)
        self.rect=self.image.get_rect()
        self.rect.x=300
        self.rect.y=330

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x +=4
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -=4
        if key_pressed[pygame.K_UP]:
            self.rect.y -=4
        if key_pressed[pygame.K_DOWN]:
            self.rect.y +=4
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

running=True
#遊戲迴圈
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():#取得電腦操作的事件
        if event.type==pygame.QUIT:
            running=False
    #更新遊戲
    all_sprites.update()

    #畫面顯示   
    screen.blit(maze,(0,0))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
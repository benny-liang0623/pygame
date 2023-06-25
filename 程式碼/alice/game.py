
import pygame
from PIL import Image
from pygame import key
import random


images=[]
FPS=60 #每秒迴圈運轉次數
WIDTH=500
HEIGHT=700
g=(0,255,0)
bg=(55,86,75)
alice=pygame.image.load('C://Users//user//Desktop//PYTHON/pygame/img/alice.png')
cake=pygame.image.load('C://Users//user//Desktop//PYTHON/pygame/img/cake.png')
bullet=pygame.image.load('C://Users//user//Desktop//PYTHON/pygame/img/agif.gif')



#遊戲初始畫面
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HungryAlice")
clock=pygame.time.Clock()
#sprite-代表遊戲內建的東西

class Player(pygame.sprite.Sprite):#設定ALICE物件
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(alice,(80,80))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-10
        self.speed=10
        

    def update(self):
        if self.rect.x==500:
            self.rect.x=0
            
        if self.rect.x==-80:
           self.rect.x=500
        
        if self.rect.top >=HEIGHT - self.rect.height:
           self.rect.top = HEIGHT - self.rect.height
        if self.rect.bottom <=self.rect.height:
           self.rect.bottom =self.rect.height
        

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x +=self.speed
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -=self.speed
        if key_pressed[pygame.K_UP]:
            self.rect.y -=self.speed
        if key_pressed[pygame.K_DOWN]:
            self.rect.y +=self.speed

    def shoot(self):
        bullet=BULLET(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
    
class Cake(pygame.sprite.Sprite):#設定CAKE物件
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(cake,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(2,10)
        self.speedx=random.randrange(-2,2)
    def update(self):
        self.rect.y +=self.speedy
        self.rect.x +=self.speedx
        if self.rect.top >=HEIGHT or self.rect.left> WIDTH or self.rect.right<0:
            self.rect.x=random.randrange(0,WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(2,10)
            self.speedx=random.randrange(-2,2)
class BULLET(pygame.sprite.Sprite):#設定BULLET物件
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bullet,(80,80))
        self.rect=self.image.get_rect()
        self.rect.centerx= x
        self.rect.bottom= y
        self.speedy=-10
    def update(self):
       self.rect.y+=self.speedy
       if self.rect.bottom<0:
           self.kill()
    


        

all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
for i in range(10):
    c=Cake()
    all_sprites.add(c)

running=True
#遊戲迴圈
while running:
    clock.tick(FPS)
    #取得輸入
    for event in pygame.event.get():#取得電腦操作的事件
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:#keydown,k_space是指按下空白建
            if event.key==pygame.K_SPACE:
                player.shoot()



    #更新遊戲
    all_sprites.update()

    #畫面顯示   
    screen.fill(bg)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
import pygame
from dataclasses import dataclass

pygame.init()

screen = pygame.display.set_mode((1000,500))

@dataclass
class Sprite:
    position: tuple
    velocity:tuple = (0,0)
    acceleration:tuple = (0,0)
PLAYER_RADIUS = 25 #設定圓形
PLAYER_COLOR = (255,0,0)#設定紅色
PLAYER_INITIAL_POS = (300,475)#設定角色位置
player = Sprite(PLAYER_INITIAL_POS)
PLAYER_JUMP_VELOCITY = (0,-500)
GRAVITY = (0,9.81)

def add_tuple(a,b): #將兩個二維向量相加
    x = a[0]+b[0]
    y = a[1]+b[1]
    return(x,y) 

def subtract_tuple(a,b): #將兩個二維向量相減
    x = a[0]-b[0]
    y = a[1]-b[1]
    return(x,y)

def times_tuple_constant(t,c):
    x = t[0]*c
    y = t[1]*c
    return(x,y)

def draw_player():
    pygame.draw.circle(screen,PLAYER_COLOR,player.position,PLAYER_RADIUS)

def update_player(t_elapse):
    #更新角色位置(S=V0*t+1/2*at^2)
    diff = times_tuple_constant(player.velocity, t_elapse)
    diff = add_tuple(diff,times_tuple_constant(player.acceleration,t_elapse**2/2 ))
    player.position = add_tuple(player.position, diff)
    #更新速度
    player.velocity = add_tuple(player.velocity,times_tuple_constant(player.acceleration, t_elapse))

    #更新加速度
    if player.position[1] < PLAYER_INITIAL_POS[1]:
        #小恐龍起跳時
        player.acceleration = add_tuple(player.acceleration, GRAVITY)
    if player.position[1] > PLAYER_INITIAL_POS[1]:
        #小恐龍掉到地板
        player.position = PLAYER_INITIAL_POS
        player.acceleration = (0,0)
        player.velocity = (0,0)


running = True
t_pre = pygame.time.get_ticks()#遊戲開始的時間

while running:#關掉視窗停止遊戲
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:#設定起跳按鍵
            player.velocity = add_tuple(player.velocity,PLAYER_JUMP_VELOCITY)


    screen.fill((0,0,0))#遊戲開始的背景黑屏
    t_cur =  pygame.time.get_ticks()#遊戲進行的時間
    update_player((t_cur - t_pre)*10**-3)
    draw_player()
    pygame.display.update()#將每一幀的畫面更新
    t_pre = t_cur

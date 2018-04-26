# 基本的元素
BACKGROUND_PATH = './assets/sprites/background-black.png'
PIPE_PATH = './assets/sprites/pipe-green.png'
BASE_PATH = './assets/sprites/base.png'
PLAYER_PATH = (
        './assets/sprites/redbird-upflap.png',
        './assets/sprites/redbird-midflap.png',
        './assets/sprites/redbird-downflap.png'
)
score = (
        './assets/sprites/0.png',
        './assets/sprites/1.png',
        './assets/sprites/2.png',
        './assets/sprites/3.png',
        './assets/sprites/4.png',
        './assets/sprites/5.png',
        './assets/sprites/6.png',
'./assets/sprites/7.png',
'./assets/sprites/8.png',
'./assets/sprites/9.png',
)
SCREENWIDTH  = 288
SCREENHEIGHT = 512
PIPEGAPSIZE=100
IMAGES = {}
BASEY=SCREENHEIGHT * 0.79
import pygame
from pygame.locals import *
from sys import exit #引入sys中exit函数
import random
#初始化pygame,为使用硬件做准备
pygame.init()

#创建了窗口
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

#设置窗口标题
pygame.display.set_caption("Flappy Bird")

#load图像，convert vs convert_alpha!
IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()
IMAGES['base'] = pygame.image.load(BASE_PATH).convert_alpha()
IMAGES['bird'] = (
    pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
)
IMAGES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE_PATH).convert_alpha(), 180),
    pygame.image.load(PIPE_PATH).convert_alpha()
)
IMAGES['score'] = (pygame.image.load(score[0]).convert_alpha(),
pygame.image.load(score[1]).convert_alpha(),pygame.image.load(score[2]).convert_alpha(),
pygame.image.load(score[3]).convert_alpha(),pygame.image.load(score[4]).convert_alpha(),
pygame.image.load(score[5]).convert_alpha(),pygame.image.load(score[6]).convert_alpha(),
pygame.image.load(score[7]).convert_alpha(),pygame.image.load(score[8]).convert_alpha(),
pygame.image.load(score[9]).convert_alpha(),
   )

PIPE_WIDTH = IMAGES['pipe'][0].get_width()
PIPE_HEIGHT = IMAGES['pipe'][0].get_height()
x=1/2*SCREENWIDTH
y=1/2*SCREENHEIGHT
move_x=0
move_y=0
flap=0
def get_RandomPipe():
    gapYs=[20,30,40,50,60,70,80,90,100,120]
    index=random.randint(0,len(gapYs)-1)
    gapY=gapYs[index]
    pipex=SCREENWIDTH+10
    gapY += int(BASEY * 0.2)
    return [{'x':pipex,'y':gapY-PIPE_HEIGHT},{'x':pipex,'y':gapY+PIPEGAPSIZE}]
pipeve1x=-4
playery=20
playerVelY=0
playerMaxVelY=-8
playerAccY=2
playerFlapAcc=-3
playerFlapped=False
newpipe1=get_RandomPipe()
upperPipes=[{'x':SCREENWIDTH,'y':newpipe1[0]['y']}]
lowerPipes=[{'x':SCREENWIDTH,'y':newpipe1[1]['y']}]
fps=60
fpsclock=pygame.time.Clock()
i=1
a=1

while True:
    for u,l in zip(upperPipes,lowerPipes):
        u['x']+=pipeve1x
        l['x']+=pipeve1x
#管道位置
    if 0<upperPipes[0]['x']<5:
        newpip=get_RandomPipe()
        upperPipes.append(newpip[0])
        lowerPipes.append(newpip[1])
       
    if upperPipes[0]['x']<-PIPE_WIDTH:
        upperPipes.pop(0)
        lowerPipes.pop(0)
#小鸟朝两管道中心移动
    if  playery >lowerPipes[0]['y']-int(PIPEGAPSIZE/2):
        input_action=0
    elif  playery <lowerPipes[0]['y']-int(PIPEGAPSIZE/2):
        input_action=1
    if input_action==0:
        playerVelY=playerFlapAcc
    elif input_action==1:
        playerVelY=playerAccY
    playery+=playerVelY  
#与键盘操作相关的，可将Y换成playery   
#    for event in pygame.event.get():
#           exit()
 #       elif event.type==KEYDOWN:
 #           if event.key==K_LEFT:
  #              move_x=-3
 #           elif event.key==K_RIGHT:
 #               move_x=3
 #           elif event.key==K_UP:
 #               move_y=-3
  #          elif event.key==K_DOWN:
 #               move_y=3
   #     elif event.type==KEYUP:
   #         move_x=0
    #        move_y=0
   # x=x + move_x
   # y=y + move_y
    if x>SCREENWIDTH:
        x=0
    elif x<0:
        x=SCREENWIDTH
    if playery>SCREENHEIGHT:
        playery=0
    elif playery<0:
        playery=SCREENHEIGHT

    # background
    SCREEN.blit(IMAGES['background'], (0,0))
    for u,l in zip(upperPipes,lowerPipes):
        SCREEN.blit(IMAGES['pipe'][0], (u['x'],u['y']))
        SCREEN.blit(IMAGES['pipe'][1], (l['x'],l['y']))
    
    SCREEN.blit(IMAGES['score'][i], (SCREENWIDTH/2,SCREENHEIGHT/4))
    if a >=9:
        SCREEN.blit(IMAGES['score'][a//10], (SCREENWIDTH/2-20,SCREENHEIGHT/4)) 
    if SCREENWIDTH/2-5<upperPipes[0]['x']+PIPE_WIDTH<SCREENWIDTH/2:
        i=i+1
        a=a+1
    if i%10==0:
        i=0
    
   
        
    SCREEN.blit(IMAGES['bird'][flap],(x,playery))
    flap=flap+1
    if flap%3==0:
        flap=0
    pygame.display.update()
    #刷新一下画面
    fpsclock.tick(fps)

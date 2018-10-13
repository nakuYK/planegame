import pygame
from plane_sprites import *

pygame.init()
#创建窗口
screen=pygame.display.set_mode((480,700))
#加载背景图像
bg=pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()
#加载飞机图像
plane=pygame.image.load("./images/me1.png")
screen.blit(plane,(185,500))
pygame.display.update()
#创建时钟对象
clock=pygame.time.Clock()
#定义rect记录飞机初始位置
plane_rect=pygame.Rect(185,500,102,126)

#导入敌机类
enemy=GameSprites("./images/enemy1.png")
enemy1=GameSprites("./images/enemy1.png",2)
enemy_group=pygame.sprite.Group(enemy,enemy1)

#游戏循环
while True:
    #游戏循环内部执行频率
    clock.tick(60)
    #监听退出事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()
    #修改飞机位置
    plane_rect.y -= 1
    if plane_rect.y+plane_rect.height<=0:
        plane_rect.y=700
    #绘制修改后图像
    screen.blit(bg,(0,0))
    screen.blit(plane,plane_rect)

    #敌机组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)

    #更新显示
    pygame.display.update()
pygame.quit()
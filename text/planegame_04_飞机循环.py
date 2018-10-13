import pygame
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
#游戏循环
while True:
    #游戏循环内部执行频率
    clock.tick(60)
    #修改飞机位置
    plane_rect.y -= 1
    if plane_rect.y+plane_rect.height<=0:
        plane_rect.y=700
    #绘制修改后图像
    screen.blit(bg,(0,0))
    screen.blit(plane,plane_rect)
    #更新显示
    pygame.display.update()
pygame.quit()
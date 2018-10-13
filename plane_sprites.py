import random
import pygame
#窗口大小常量
SCREEN_RECT=pygame.Rect(0,0,480,700)
#刷新频率常量
REFRESH_PER=60
#创建敌机定时器常量
CREATE_ENEMY_EVENT=pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT=pygame.USEREVENT+1

class GameSprites(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self):
        self.rect.y+=self.speed

class Background(GameSprites):
    """游戏背景精灵"""
    def __init__(self,is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y= -self.rect.height

    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y= -self.rect.height

class Enemy(GameSprites):
    """敌机精灵"""
    def __init__(self):
        #调用父类方法，创建敌机精灵
        super().__init__("./images/enemy1.png")
        #指定敌机的初始随机速度
        self.speed=random.randint(1,3)
        #指定敌机的初始随机位置
        self.rect.bottom=0
        max_x=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(0,max_x)
    def update(self):
        #调用父类方法，保持垂直方向飞行
        super().update()
        #判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕")
            #kill方法可以将精灵从所有精灵组中删除
            self.kill()
    def __del__(self):
        #print("删除敌机",self.rect)
        pass

class Hero(GameSprites):
    """英雄精灵"""
    def __init__(self):
        #调用父类方法，设置image和speed
        super().__init__("./images/me1.png",0)
        #设置初始位置
        self.rect.centerx=SCREEN_RECT.centerx
        self.rect.bottom=SCREEN_RECT.bottom-50
        #创建子弹精灵组
        self.bullets=pygame.sprite.Group()
    def update(self):
        #英雄在水平方向移动
        self.rect.x += self.speed
        #英雄不能超出屏幕
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right
    def fire(self):
        #print("发射子弹")
        for i in (0,1,2):
            bullet=Bullet()
            bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.centerx=self.rect.centerx
            self.bullets.add(bullet)

class Bullet(GameSprites):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)
    def update(self):
        super().update()
        #判断是否飞出屏幕
        if self.rect.bottom<0:
            self.kill()
    def __del__(self):
        #print("子弹删除")
        pass

import pygame
from plane_sprites import *

class PlaneGame(object):
    def __init__(self):
        print("..游戏初始化..")
        #创建游戏窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock=pygame.time.Clock()
        #创建精灵和精灵组
        self.__create_sprites()
        #设置定时器事件 - 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1200)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1=Background()
        bg2=Background(is_alt=True)
        self.back_group=pygame.sprite.Group(bg1,bg2)
        #创建敌机精灵组
        self.enemy_group=pygame.sprite.Group()
        #创建英雄精灵和精灵组
        self.hero=Hero()
        self.hero_group=pygame.sprite.Group(self.hero)

    def game_start(self):
        print("...游戏开始...")
        while True:
            #1.设置刷新频率
            self.clock.tick(REFRESH_PER)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.绘制/更新精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type==CREATE_ENEMY_EVENT:
                #print("敌机出场")
                #创建敌机精灵
                enemy=Enemy()
                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type==HERO_FIRE_EVENT:
                self.hero.fire()
        #按键捕获
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed=2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed=-2
        else:
            self.hero.speed=0

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        #敌机撞毁英雄
        enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("...游戏结束...")
        pygame.quit()
        exit()

if __name__ == '__main__':
    #
    game=PlaneGame()
    #
    game.game_start()
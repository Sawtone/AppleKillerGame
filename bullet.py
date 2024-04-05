import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, kid):
        """在kid所在位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 先在原点创建一个子弹，再设置正确的位置
        self.image = pygame.image.load('images/bullet.webp')
        if ai_settings.easy > 0:
            self.image = pygame.image.load('images/big-bullet.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = kid.rect.centerx
        self.rect.top = kid.rect.top

        # 如kid一样，存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        self.screen.blit(self.image, self.rect)

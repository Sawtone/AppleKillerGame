import pygame
from pygame.sprite import Sprite


class Kid:

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置他的初始位置"""
        super(Kid, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载kid图像并获取其外接矩形
        self.image = pygame.image.load('images/kid.jpg')
        self.rect = self.image.get_rect()        # 获取kid外接矩形
        self.screen_rect = screen.get_rect()     # 获取屏幕外接矩形

        # 将每一个kid都放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在kid的属性center中存储小数值
        self.center = float(self.rect.centerx)     # 只存整数，但问题不大

        # 设置移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志来调整kid的位置"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.kid_speed_factor
        if self.moving_left and (self.rect.left > 0):
            self.center -= self.ai_settings.kid_speed_factor

        self.rect.centerx = self.center

    def blit_1(self):
        """在指定位置绘制kid"""
        self.screen.blit(self.image, self.rect)

    def center_kid(self):
        """让kid复活"""
        self.center = self.screen_rect.centerx

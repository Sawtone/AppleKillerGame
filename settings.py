import pygame


class Settings:
    """这是一个存储游戏的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕相关设置
        self.screen_width = 1200
        self.screen_height = 750
        self.background_color = (230, 230, 230)      # 指定浅灰色为背景色

        # kid的相关设置
        self.kid_limit = 3

        # 子弹的相关设置
        self.bullets_allowed = 4

        # 苹果的相关设置
        self.apple_speed_drop = 10
        self.direction = 1

        # 加快节奏
        self.speed_up_scale = 1.18
        self.score_scale = 2
        self.round = 0
        self.easy = 0
        self.omen = 0
        self.defeat = 0
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随难度变化的设置"""
        self.image_1 = pygame.image.load('images/apple66.jpg')
        self.kid_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.apple_speed_factor = 0.5
        self.apple_points = 50


    def increase_speed(self):
        """提高速度的设置"""
        self.kid_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.apple_speed_factor *= self.speed_up_scale
        self.apple_points = int(self.apple_points * self.score_scale)
        if self.round == 2:
            self.image_1 = pygame.image.load('images/apple77.jpg')
        if self.round == 4:
            self.image_1 = pygame.image.load('images/apple88.jpg')

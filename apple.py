import pygame

from pygame.sprite import Sprite


class Apple(Sprite):
    """表示单个苹果的类"""
    def __init__(self, ai_settings, screen):
        """初始化苹果并设置起始位置"""
        super(Apple, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 设置图像并获取外接矩形数据
        self.image = ai_settings.image_1
        self.rect = self.image.get_rect()
        # 每个苹果都出现在原点附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit_1(self):
        """在指定位置绘制苹果"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """让苹果儿动起来"""
        self.x += (self.ai_settings.apple_speed_factor *
                   self.ai_settings.direction)
        self.rect.x = self.x

    def check_edges(self):
        """检测是否有苹果儿撞了南墙（返回True）"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left < 0:
            return True

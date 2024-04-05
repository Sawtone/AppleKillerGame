import pygame.font


class Button1:
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 550
        self.height = 50
        self.button_color = (230, 155, 0)
        self.text_color = (220, 220, 220)
        self.font = pygame.font.SysFont(None, 36)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg（指定文本）渲染为图像"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class Button2:
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (230, 155, 0)
        self.text_color = (220, 220, 220)
        self.font = pygame.font.SysFont(None, 24)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery + 150

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg（指定文本）渲染为图像"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
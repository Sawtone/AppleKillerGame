import pygame.font
import pygame
from pygame.sprite import Group
from kid import Kid


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分的相关属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.image = pygame.image.load('images/hide.jpg')

        # 相关字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 渲染
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_perpoint()
        self.prep_kids()
        self.prep_omen()
        self.prep_defeat()

    def prep_score(self):
        """将得分文本渲染成图像"""
        # 先将数字变成三位一单元的字符串，再传递给render渲染为图像
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.background_color)
        # 将其置于屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self):
        """将最高得分文本渲染成图像"""
        highest_score = int(round(self.stats.highest_score, -1))
        highest_score_str = "{:,}".format(highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True,
                                                    self.text_color, self.ai_settings.background_color)

        # 将其置于屏幕顶部
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级渲染成图像"""
        self.level_image = self.font.render("level:" + str(self.stats.level), True,
                                      self.text_color, self.ai_settings.background_color )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_perpoint(self):
        """将单个得分渲染为图象"""
        self.perpoint_image = self.font.render("per:" + str(self.stats.perpoint), True,
                                      self.text_color, self.ai_settings.background_color )
        self.perpoint_rect = self.perpoint_image.get_rect()
        self.perpoint_rect.right = self.score_rect.right
        self.perpoint_rect.top = self.level_rect.bottom + 10

    def prep_kids(self):
        """将kid图像渲染以表示kid的剩余生命"""
        self.kids = Group()
        for kid_number in range(self.stats.kids_left):
            kid = Kid(self.ai_settings, self.screen)
            kid.rect.x = kid_number * kid.rect.width + 10
            kid.rect.y = 10
            self.kids.add_internal(kid)

    def prep_omen(self):
        """渲染暗影精灵"""
        if self.ai_settings.omen > 0:
            self.image = pygame.image.load('images/omen.jpg')
        else:
            self.image = pygame.image.load('images/hide.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def prep_defeat(self):
        """渲染失败鼓励"""
        if self.ai_settings.defeat > 0:
            self.defeat_image = pygame.image.load('images/defeat.jpg')
        else:
            self.defeat_image = pygame.image.load('images/hide.jpg')
        self.defeat_rect = self.defeat_image.get_rect()
        self.defeat_rect.center = self.screen_rect.center

    def show_score(self):
        """在屏幕上显示得分图像"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.perpoint_image, self.perpoint_rect)
        self.kids.draw(self.screen)
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.defeat_image, self.defeat_rect)

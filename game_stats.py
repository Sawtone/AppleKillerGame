from settings import Settings
import pygame


class GameStats:
    """跟踪游戏中的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.highest_score = 0

    def reset_stats(self):
        """初始化所有统计信息"""
        self.kids_left = self.ai_settings.kid_limit
        self.score = 0
        self.level = 1
        self.perpoint = 50

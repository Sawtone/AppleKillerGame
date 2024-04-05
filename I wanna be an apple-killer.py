import pygame
import game_functions as gf

from settings import Settings
from kid import Kid
from apple import Apple
from pygame.sprite import Group
from game_stats import GameStats
from button import Button1
from button import Button2
from score_board import Scoreboard


def run_game():
    # 初始化小游戏儿、设置，并创建一个屏幕对象（screen）
    pygame.init()       # 初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))       # 用元组指定尺寸
    pygame.display.set_caption("I don't wanna be an apple-killer")     # 设置页面标题

    # 创建用于统计信息的实例和记分牌的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建小kid
    kid = Kid(ai_settings, screen)
    # 创建一个用来存储苹果儿的编组
    apples = Group()
    gf.create_apples_fleet(ai_settings, screen, kid, apples)
    # 创建一个用来存储子弹儿的编组
    bullets = Group()
    # 创建开始游戏按钮
    play_button = Button1(ai_settings, screen, "A little more touch will explode!    ( I'm ikun")
    # 创建降难按钮
    easy_button = Button2(ai_settings, screen, "If you are 250, Click me!")

    # 用于开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, kid, apples, bullets, easy_button)
        if stats.game_active:
            kid.update()
            gf.update_bullets(ai_settings, screen, stats, sb, kid, apples, bullets)
            gf.update_apples(ai_settings, screen, stats, sb, kid, apples, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, kid, apples, bullets,
                         play_button, easy_button)


run_game()      # 使用函数

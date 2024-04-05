# 存储大量游戏运行相关函数
import sys
import math
import pygame

from bullet import Bullet
from apple import Apple
from game_stats import GameStats
from time import sleep


def check_keydown_events(event, ai_settings, screen, kid, bullets):
    """响应按键行为"""
    if event.key == pygame.K_RIGHT:
        kid.moving_right = True
        kid.image = pygame.image.load('images/kidr.jpg')
    if event.key == pygame.K_LEFT:
        kid.moving_left = True
        kid.image = pygame.image.load('images/kid.jpg')
    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, kid, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def fire_bullets(ai_settings, screen, kid, bullets):
    """如果没有达到最大限制便发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, kid)
        bullets.add(new_bullet)


def check_keyup_events(event, kid):
    """响应松开行为"""
    if event.key == pygame.K_RIGHT:
        kid.moving_right = False
    if event.key == pygame.K_LEFT:
        kid.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, kid, apples, bullets, easy_button):
    """响应键盘和鼠标的事件"""
    for event in pygame.event.get():  # 事件循环
        if event.type == pygame.QUIT:  # 检测到用户单击叉号退出窗口，则调用sys退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 检测按键行为
            check_keydown_events(event, ai_settings, screen, kid, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, kid)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, kid, apples,
                              bullets, mouse_x, mouse_y, easy_button)


def check_play_button(ai_settings, screen, stats, sb, play_button, kid, apples,
                      bullets, mouse_x, mouse_y, easy_button):
    """在玩家单击开始按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    button_clicked_1 = easy_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()    # 重置设置
        pygame.mouse.set_visible(False)   # 隐藏光标
        # 重置所有统计信息
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_highest_score()
        sb.prep_level()
        sb.prep_perpoint()
        sb.prep_kids()
        apples.empty()
        bullets.empty()
        create_apples_fleet(ai_settings, screen, kid, apples)
        kid.center_kid()
    if button_clicked_1 and not stats.game_active:
        ai_settings.easy += 1


def update_screen(ai_settings, screen, stats, sb, kid, apples, bullets,
                  play_button, easy_button):
    """更新屏幕上的图像，并重绘屏幕"""
    # 每次while循环都重新绘制屏幕
    screen.fill(ai_settings.background_color)   # 用指定的背景色填充屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    kid.blit_1()
    apples.draw(screen)   # 绘制编组的每一个元素
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
        easy_button.draw_button()

    # 让最近一次绘制的screen可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, kid, apples, bullets):
    """管理子弹，更新子弹位置并及时删除部分子弹"""
    bullets.update()
    # 删除画面外的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_apple_collisions(ai_settings, screen, stats, sb, kid, apples, bullets)


def check_bullet_apple_collisions(ai_settings, screen, stats, sb, kid, apples, bullets):
    # 有子弹击中苹果，就删除对应的子弹和苹果
    collisions = pygame.sprite.groupcollide(bullets, apples, True, True)
    if collisions:
        for apples in collisions.values():
            stats.score += ai_settings.apple_points
            sb.prep_score()
        check_highest_score(stats, sb)
    # 如果苹果没了，就删除现有子弹并创建苹果
    if len(apples) == 0:
        sb.ai_settings.omen += 1
        sb.prep_omen()
        sb.show_score()
        pygame.display.flip()
        bullets.empty()
        stats.level += 1
        sb.prep_level()
        stats.perpoint = int(50 * (math.pow(ai_settings.score_scale, stats.level)) * 0.5)
        sb.prep_perpoint()
        ai_settings.round += 1
        ai_settings.increase_speed()
        sleep(2)
        sb.ai_settings.omen -= 1
        sb.prep_omen()
        sb.show_score()
        pygame.display.flip()
        create_apples_fleet(ai_settings, screen, kid, apples)


def get_number_apples_x(ai_settings, apple_width):
    """初步获取每行的苹果个数"""
    # 间距为图片外接矩形宽度
    available_space_x = ai_settings.screen_width - 2 * apple_width
    numbers_apples_x = int(available_space_x / (2 * apple_width))
    return numbers_apples_x


def get_number_apples_rows(ai_settings, kid_height, apple_height):
    """初步计算屏幕可容纳多少苹果"""
    available_space_y = (ai_settings.screen_height -
                         (3 * apple_height) - kid_height)
    number_rows = int(available_space_y) / (2 * apple_height)
    return number_rows


def create_apple(ai_settings, screen, apples, apple_number, row_number):
    """创建一个苹果儿并放在当前行"""
    apple = Apple(ai_settings, screen)
    apple_width = apple.rect.width
    if row_number == 0:
        apple.x = 4 * apple_width + 2 * apple_width * apple_number
    elif row_number == 2:
        apple.x = 2 * apple_width + 2 * apple_width * apple_number
    elif row_number == 3:
        apple.x = 1 * apple_width + 2 * apple_width * apple_number
    else:
        apple.x = 3 * apple_width + 2 * apple_width * apple_number
    apple.y = 1 * apple.rect.height + 1 * apple.rect.height * row_number
    apple.rect.x = apple.x
    apple.rect.y = apple.y
    apples.add(apple)


def create_apples_fleet(ai_settings, screen, kid, apples):
    """创建苹果群"""
    apple = Apple(ai_settings, screen)
    number_apples_x = get_number_apples_x(ai_settings, apple.rect.width)
    number_rows = get_number_apples_rows(ai_settings, kid.rect.height,
                                         apple.rect.height)
    number_rows_int = int(number_rows) - 1
    for row_number in range(number_rows_int):
        for apple_number in range(number_apples_x - 3):
            # 每次创建一个并加入当前行
            create_apple(ai_settings, screen, apples, apple_number, row_number)


def kid_hit(ai_settings, screen, stats, sb, kid, apples, bullets):
    """响应被苹果撞到的kid"""
    if stats.kids_left > 0:
        stats.kids_left -= 1
        sb.prep_kids()
        apples.empty()
        bullets.empty()
        sb.ai_settings.defeat += 1
        sb.prep_defeat()
        sb.show_score()
        pygame.display.flip()
        ai_settings.round = 0
        sleep(3)
        sb.ai_settings.defeat -= 1
        sb.prep_defeat()
        sb.show_score()
        pygame.display.flip()
        create_apples_fleet(ai_settings, screen, kid, apples)
        kid.center_kid()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_apple_bottom(ai_settings, screen, stats, sb, kid, apples, bullets):
    """检查是否有苹果到达屏幕底端"""
    screen_rect = screen.get_rect()
    for apple in apples.sprites():
        if apple.rect.bottom >= screen_rect.bottom:
            kid_hit(ai_settings, screen, stats, sb, kid, apples, bullets)
            break


def update_apples(ai_settings, screen, stats, sb, kid, apples, bullets):
    """检查是否有苹果撞墙，并更新苹果堆里所有苹果的位置"""
    check_apples_edges(ai_settings, apples)
    apples.update()
    # 检查苹果是否撞到kid
    if pygame.sprite.spritecollideany(kid, apples):
        kid_hit(ai_settings, screen, stats, sb, kid, apples, bullets)
    # 检查苹果是否到达屏幕底端
    check_apple_bottom(ai_settings, screen, stats, sb, kid, apples, bullets)


def check_apples_edges(ai_settings, apples):
    """有苹果撞墙时采取行动"""
    for apple in apples.sprites():
        if apple.check_edges():
            change_apple_direction(ai_settings, apples)
            break


def change_apple_direction(ai_settings, apples):
    """使苹果下移并转向"""
    for apple in apples.sprites():
        apple.rect.y += ai_settings.apple_speed_drop
    ai_settings.direction *= -1


def check_highest_score(stats, sb):
    """检查是否有新的最高得分出现"""
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        sb.prep_highest_score()

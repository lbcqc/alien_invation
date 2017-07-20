import sys
import pygame
import game_function as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()

	# 导入设置参数
	my_settings = Settings()
	# 初始化屏幕并设置
	pygame.display.set_caption(my_settings.title)
	screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
	
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(my_settings)
	
	# 创建一艘飞船
	ship = Ship(my_settings, screen)
	
    # 创建子弹组
	bullets = Group()

    # 创建初始外星人族群
	aliens = Group()
	gf.create_fleet(my_settings, screen, ship, aliens)

	# 创建Play按钮
	play_button = Button(my_settings, screen, "Play")

	# 创建记分牌
	sb = Scoreboard(my_settings, screen, stats)


	# 开始游戏的主循环
	while True:
		gf.check_event(my_settings, stats, screen, sb, ship, bullets, play_button)
		if stats.game_active:
			ship.update()
			gf.update_bullet(my_settings, stats, screen, sb, ship, aliens, bullets)
			gf.update_aliens(my_settings, stats, screen, sb, ship, aliens, bullets)
		gf.update_screen(my_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
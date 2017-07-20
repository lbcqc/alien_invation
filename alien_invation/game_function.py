import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from scoreboard import Scoreboard

def check_keydown_events(event, settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_play_button(stats, sb, play_button, mouse_x, mouse_y):
	if stats.game_active == False and play_button.rect.collidepoint(mouse_x, mouse_y):
		stats.game_active =True
		stats.reset_stats()
		
		# 重置计分板图像
		sb.prep_score()
		sb.prep_level()
		sb.prep_ships_left()

		print "new game start!!!"
		pygame.mouse.set_visible(False)

def check_event(settings, stats, screen, sb, ship, bullets, play_button):
	# 响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, sb, play_button, mouse_x, mouse_y)
		else:
			pass

def update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button):
	# 每次循环时重绘制屏幕
	screen.fill(settings.bg_color)
	# 在飞船和外星人前面重绘所有子弹
	sb.show_score()
	if stats.game_active:
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		ship.blitme()
		aliens.draw(screen)
	else:
		play_button.draw_button()
	
	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullet(settings, stats, screen, sb, ship, aliens, bullets):
	bullets.update()
	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#检测子弹和外星人的碰撞
	check_bullet_alien_collisions(settings, screen, stats, sb, ship, bullets, aliens)
	

def check_bullet_alien_collisions(settings, screen, stats, sb, ship, bullets, aliens):
	# 检测是否击中外星人
	# 如果击中则删除相应的子弹和外星人
	old_len = len(aliens)
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	new_len = len(aliens)
	if new_len<old_len:
		stats.score += settings.alien_points * (old_len-new_len)
		sb.prep_score()
	# 检测外星族群是否被消灭
	# 如果是则创建新族群
	if len(aliens) == 0:
		bullets.empty()
		settings.increase_speed()
		create_fleet(settings, screen, ship, aliens)

		# 提升等级
		stats.level += 1
		sb.prep_level();

def fire_bullet(settings, screen, ship, bullets):
	# 创建一颗子弹并加入到编组bullets中
	if int(len(bullets)) < settings.bullets_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)

#获取一行可放置的外星人数量
def get_number_aliens_x(settings, screen):
	# 创建一个外星人样例获取数据
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	available_space_x = settings.screen_width -2 * alien_width
	return int(available_space_x / (2 * alien_width))

# 获取屏幕可容下多少行外星人
def get_number_aliens_y(settings, screen, ship):
	# 创建一个外星人样例获取数据
	alien = Alien(settings, screen)
	alien_height = alien.rect.height
	available_space_y = settings.screen_height - 3 * alien_height - ship.rect.height
	return int(available_space_y / (2 * alien_height))

# 在当前行放置一个外星人
def create_alien(settings, screen, aliens, alien_number, alien_row):
	alien = Alien(settings, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.y = alien_height + 2 * alien_height * alien_row
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
	number_aliens_y = get_number_aliens_y(settings, screen, ship)
	number_aliens_x = get_number_aliens_x(settings, screen)
	# 创建外星人族群
	for alien_row in range(number_aliens_y):
		#创建一行外星人
		for alien_number in range(number_aliens_x):
			# 创建一个外星人
			create_alien(settings, screen, aliens, alien_number, alien_row)

# 更新外星人族群，使其移动
def update_aliens(settings, stats, screen, sb, ship, aliens, bullets):
	# 检测外星人族群是否遇到左右边界
	check_fleet_edges(settings, aliens)
	aliens.update()
	
	# 检测外星人与飞船之间是否发生碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(settings, stats, screen, sb, ship, aliens, bullets)

	# 检测外星人是否碰到屏幕底端
	check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets)

# 检测外星人族群是否遇到边界
def check_fleet_edges(settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

# 检测外星人是否碰到屏幕底端
def check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 像飞船被撞到一样进行处理
			ship_hit(settings, stats, screen, sb, ship, aliens, bullets)
			break

def change_fleet_direction(settings, aliens):
	# 将外星人整体下移并且改变他们的移动方向
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1

def ship_hit(settings, stats, screen, sb, ship, aliens, bullets):
	if stats.ships_left <= 1:
		stats.game_active = False

	if stats.game_active == False:
		print "game over"
		settings.initialize_dynamic_settings()

		# 重置最高分
		if stats.score > stats.high_score:
			stats.high_score = stats.score
			print "Congratulation, you get the highest marks!!!"
			sb.prep_high_score()
			sb.show_score()

		pygame.mouse.set_visible(True)
	else:
		print "Ship hit!!!"

	# 相应被外星人撞到的飞船
	stats.ships_left -= 1
	sb.prep_ships_left()

	# 清空外星人列表和子弹列表
	aliens.empty()
	bullets.empty()

	# 创建一群新的外星人， 并将飞船放到屏幕底端中央
	create_fleet(settings, screen, ship, aliens)
	ship.center_ship()

	# 暂停
	sleep(0.5)
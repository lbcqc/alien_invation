import pygame.font

class Scoreboard(object):
	def __init__(self, settings, screen, stats):
	    # 显示得分信息的类
	    self.screen = screen
	    self.screen_rect = screen.get_rect()
	    self.settings = settings
	    self.stats = stats

	    # 显示得分信息时使用的字体设置
	    self.text_color = (30,30,30)
	    self.font = pygame.font.SysFont(None, 48)

	    # 准备初始得分图像
	    self.prep_score()
	    self.prep_high_score()
	    self.prep_level()
	    self.prep_ships_left()

	def prep_score(self):
		# 将得分转化为一幅渲染的图像
		rounded_score = int(round(self.stats.score, -1))
		score_str = "score : " + "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color,
									  self.settings.bg_color)

		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		# 将最高分渲染为图像
		high_score = int(round(self.stats.high_score, -1))
		high_str = "highscore : " + "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_str, True, self.text_color,
									  self.settings.bg_color)

		# 显示在顶部中央
		self.high_rect = self.high_score_image.get_rect()
		self.high_rect.centerx = self.screen_rect.centerx
		self.high_rect.top = self.score_rect.top
		
	def prep_level(self):
		# 将等级转化为渲染的图像
		level_str = "level : " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color,
									  self.settings.bg_color)

		# 设置等级图像的显示位置
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships_left(self):
		ships_left_str = "ship-left : " + str(self.stats.ships_left)
		self.ships_left_image = self.font.render(ships_left_str, True, self.text_color,
									  self.settings.bg_color)

		# 设置剩余飞船图像的显示位置
		self.ships_left_rect = self.ships_left_image.get_rect()
		self.ships_left_rect.left = self.screen_rect.left + 20
		self.ships_left_rect.top = self.score_rect.top

	def show_score(self):
		# 在屏幕上显示得分
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.ships_left_image, self.ships_left_rect)

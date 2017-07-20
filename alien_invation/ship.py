import pygame
class Ship(object):
	def __init__(self, settings, screen):
		# 初始化飞船并设置初始位置
		self.screen = screen

		# 初始化移动标志
		self.moving_right = False
		self.moving_left = False
		self.settings = settings
		

		# 加载飞船图像并获取其外接矩阵
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将每艘新飞船加载在屏幕底端
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#将飞船位置保存为小数值
		self.center = float(self.rect.centerx)

	def blitme(self):
		# 在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)

	def update(self):
		# 根据移动标志移动
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0: # 为确保左右键同时按下时工作正常，不能使用elif
			self.center -= self.settings.ship_speed_factor
		
		# 更新位置
		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx
		self.rect.centerx = self.center
		self.rect.bottom = self.screen_rect.bottom
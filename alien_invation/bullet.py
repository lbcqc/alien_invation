import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		# 创建一个子弹矩阵
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储用小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor

	def update(self):
		# 向上移动子弹
		self.y -= self.speed_factor
		# 更新子弹的rect位置
		self.rect.y = self.y

	def draw_bullet(self):
		# 在屏幕上绘制子弹
		pygame.draw.rect(self.screen, self.color, self.rect)
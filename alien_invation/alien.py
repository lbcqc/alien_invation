import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # 加载外星人图像, 并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附加
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

	    # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 在指定外置绘制外星人
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
        	return True
        elif self.rect.left <= 0:
        	return True
        else:
        	return False
class Settings(object):

	def initialize_dynamic_settings(self):
		# 初始化动态参数
		self.ship_speed_factor = 1.0
		self.alien_speed_factor = 1 # 横移动速度
		self.fleet_drop_speed = 10  # 向下移动速度
		self.fleet_direction = 1    # 1表示向右移动，为-1表示向下移动

		# 外星人分数
		self.alien_points = 50

	
	def increase_speed(self):
		# 等级提升
		self.ship_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.fleet_drop_speed *= self.speedup_scale
		self.alien_points *= self.score_scale

	def __init__(self):

		# ship
		self.ship_limit = 3
		
		# 标题
		self.title = 'Alien Invation'

		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230, 230, 230) # 浅白色-背景
		
        # 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# 以一个速度加快游戏进度
		self.speedup_scale = 1.1

		# 外星人的点数提升速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
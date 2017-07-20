class GameStats(object):
    def __init__(self, my_settings):
		self.settings = my_settings
		self.game_active = False
		self.reset_stats()
		self.high_score = 0
		
    def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
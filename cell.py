import pygame

class Cell(pygame.sprite.Sprite):
	def __init__(self, alive, pos, size):
		super().__init__()
		self.alive = alive
		self.image = pygame.Surface((size, size))
		self.image.fill('black' if self.alive else 'white')
		self.rect = self.image.get_rect(topleft = pos)

	def update(self):
		self.image.fill('black' if self.alive else 'white')

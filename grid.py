from cell import Cell
import pygame, random

ROWS, COLS = 100, 100
CELL_SIZE = 10

class Grid:
	def __init__(self):
		self.cells = pygame.sprite.Group()
		self.grid = [[Cell(random.randrange(1, 100) >= 80, (x * CELL_SIZE, y * CELL_SIZE), CELL_SIZE) for y in range(COLS)] for x in range(ROWS)]
		self.cells.add(self.grid)
		self.next_gen = [[False for _ in range(COLS)] for _ in range(ROWS)]

	def update(self):
		self.get_next_gen()				

	def get_next_gen(self):
		self.make_next_gen()
		self.apply_next_gen()

	def make_next_gen(self):
		for col in range(COLS):
			for row in range(ROWS):
				alive_neigbors = self.get_living_neighbors(row, col)
				cell_liveness = self.grid[row][col].alive

				if cell_liveness and alive_neigbors < 2:
					cell_liveness = False
				elif cell_liveness and alive_neigbors < 4:
					pass
				elif cell_liveness:
					cell_liveness = False
				elif alive_neigbors == 3:
					cell_liveness = True

				self.next_gen[row][col] = cell_liveness

	def apply_next_gen(self):
		for col in range(COLS):
			for row in range(ROWS):
				self.grid[row][col].alive = self.next_gen[row][col]
				self.grid[row][col].update()

	def get_living_neighbors(self, row, col):
		alive_neigbors = 0

		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == j == 0:
					continue
				x, y = clamp_rev(row + i, 0, ROWS - 1), clamp_rev(col + j, 0, COLS - 1)
				if self.grid[x][y].alive:
					alive_neigbors += 1

		return alive_neigbors

def clamp_rev(num, min_num, max_num):
	if num < min_num:
		num = max_num
	elif num > max_num:
		num = min_num
	return num

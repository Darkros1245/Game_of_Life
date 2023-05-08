import pygame, sys
from grid import Grid

pygame.init()

WIDTH, HEIGHT = 1000, 1000

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Life')
clock = pygame.time.Clock()

def main():
	surface = pygame.Surface(window.get_size())
	surface = surface.convert()

	grid = Grid()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		grid.cells.draw(surface)
		window.blit(surface, (0, 0))
		pygame.display.update()
		grid.update()
		clock.tick(60)

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()

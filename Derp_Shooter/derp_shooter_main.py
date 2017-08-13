import pygame
from input_handler import *
from object_handler import *
import buffer
pygame.init()
dimension = (800, 600)
gameDisplay = pygame.display.set_mode(dimension)
pygame.display.set_caption("Derp Shooter")

buffer.test()
clock = pygame.time.Clock()

quitting = False

while not quitting:
	gameDisplay.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitting = True
		input_handler(event)
	


	object_handler(gameDisplay)

	
	pygame.display.update()
	clock.tick(60)


pygame.quit()
quit()


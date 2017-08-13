import pygame
def sprite(x, y, img, display):
	img_wrap = pygame.image.load(img)
	display.blit(img_wrap, (x, y))
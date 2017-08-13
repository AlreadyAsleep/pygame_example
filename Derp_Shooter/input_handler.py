import pygame
import buffer

control = {"up": pygame.K_UP,
		   "down": pygame.K_DOWN, 
		   "right": pygame.K_RIGHT, 
		   "left": pygame.K_LEFT}

input_obj = [buffer.red]

def input_handler(event):
	for i in input_obj:
		if event.type == pygame.KEYDOWN:
			if event.key == control['up']:
				i.change_velocity(0, -1)
			if event.key == control['down']:
				i.change_velocity(0, 1)
			if event.key == control['right']:
				i.change_velocity(1, 0)
			if event.key == control['left']:
				i.change_velocity(-1, 0)
		

import pygame
from sprite_loader import *
objLoader = []

class game_object:

	x = 0
	y = 0
	img = ""
	velx = 0
	vely = 0

	def __init__ (self, x, y, img):
		self.x, self.y, self.img = x, y, img

	def change_velocity(self, xChange, yChange):
		self.velx += xChange
		self.vely += yChange

	def velocity(self):
		self.x += self.velx
		self.y += self.vely

def add_object(*game_object):
	for o in game_object:
		objLoader.append(o)

def remove_object(*game_object):
	for o in game_object:
		objLoader.remove(o)

def object_handler(display):
	for o in objLoader:
		sprite(o.x, o.y, o.img, display)
		o.velocity()

import pygame
import random

class Block:
	def determineColor(self):
		red = random.randint(155, 255)
		green = random.randint(155, 255)
		blue = random.randint(155, 255)
		if red >= green or blue >= green:
			green = 0
		if green >= red or blue >= red:
			red = 0
		if red >= blue or green >= blue:
			blue = 0
		return (red, green, blue)

	def __init__(self, x, y):
		self.sprite = pygame.image.load('./Sprites/ball.png')
		self.height = self.sprite.get_height()
		self.width = self.sprite.get_width()
		self.x = x
		self.y = y
		#bright colors
		self.color = self.determineColor()
		# self.color = (random.randint(155,255), random.randint(155,255), random.randint(155,255))
		self.sprite = self.sprite.copy()
		self.sprite.fill((0, 0, 0, 0), None, pygame.BLEND_RGBA_MULT)
		self.sprite.fill(self.color, None, pygame.BLEND_RGBA_ADD)

	def update(self):
		pass


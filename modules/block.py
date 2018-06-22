import pygame
import random
import modules.rect as rect

class Block(rect.Rect):
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

	def __init__(self, x, y, spriteName):
		rect.Rect.__init__(self, x, y, spriteName)
		self.color = self.determineColor()
		self.sprite = self.sprite.copy()
		self.sprite.fill((0, 0, 0, 0), None, pygame.BLEND_RGBA_MULT)
		self.sprite.fill(self.color, None, pygame.BLEND_RGBA_ADD)
import pygame
import random
import modules.rect as rect

class Player(rect.Rect):
	def __init__(self, x, y, spriteFile, displayWidth, displayHeight):
		rect.Rect.__init__(self, x, y, spriteFile)
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		self.speedIncrease = 10
		self.xSpeed = 0
		self.ySpeed = 0
		self.up = False
		self.down = False

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and self.up == False:
					self.ySpeed += -self.speedIncrease
					self.up = True
				elif event.key == pygame.K_DOWN and self.down == False:
					self.ySpeed += self.speedIncrease
					self.down = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.ySpeed += self.speedIncrease
					self.up = False
				elif event.key == pygame.K_DOWN:
					self.ySpeed += -self.speedIncrease
					self.down = False

		if self.y + self.ySpeed > self.displayHeight - self.height:
			self.y = self.displayHeight - self.height
		elif self.y + self.ySpeed < 0:
			self.y = 0
		else:
			self.y += self.ySpeed
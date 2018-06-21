import pygame
import random

class Ball:
	def __init__(self, displayWidth, displayHeight):
		self.sprite = pygame.image.load('./Sprites/ball.png') 
		self.height = self.sprite.get_height()
		self.width = self.sprite.get_width()
		self.x = displayWidth * 0.45
		self.y = displayHeight * 0.50
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		self.xSpeed = -15
		self.ySpeed = random.randint(-5, 5) 
		self.up = False
		self.down = False
		if self.ySpeed == 0:
			self.ySpeed = -1

	def update(self):
		if self.x > 0 and self.x < self.displayWidth - self.width:
			self.x += self.xSpeed
		else:
			self.x -= self.xSpeed
			self.xSpeed *= -1

		if self.y > 0 and self.y < self.displayHeight - self.height:
			self.y += self.ySpeed
		else:
			self.y -= self.ySpeed
			self.ySpeed *= -1
		
import pygame

class Ball:
	def __init__(self, displayWidth, displayHeight):
		self.sprite = pygame.image.load('./Sprites/ball.png') 
		self.height = self.sprite.get_height()
		self.width = self.sprite.get_width()
		self.x = displayWidth * 0.45
		self.y = displayHeight * 0.50
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		self.xSpeed = 1
		self.ySpeed = 0
		self.up = False
		self.down = False

	def update(self):
		self.x += self.xSpeed
		
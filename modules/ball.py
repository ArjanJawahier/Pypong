import pygame
import random

class Ball:
	def __init__(self, displayWidth, displayHeight):
		self.sprite = pygame.image.load('./Sprites/ball.png') 
		self.height = self.sprite.get_height() 
		self.width = self.sprite.get_width() 
		self.x = displayWidth * 0.3
		self.y = displayHeight * 0.45
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
		self.xSpeed = -10
		self.ySpeed = random.randint(-3, 3)
		self.up = False
		self.down = False
		self.timesHitLeftSide = 0
		if self.ySpeed == 0:
			self.ySpeed = -1

	def update(self, blocks, player):
		if self.x > 0 and self.x < self.displayWidth - self.width:
			self.x += self.xSpeed
		else:
			if self.x <= 0:
				self.timesHitLeftSide += 1
			self.bounceX()

		if self.y > 0 and self.y < self.displayHeight - self.height:
			self.y += self.ySpeed
		else:
			self.bounceY()

		for block in blocks:
			if block.intersectBoth(self):
				if self.xSpeed <= self.ySpeed:
					self.bounceX()
				else:
					self.bounceY()
				blocks.remove(block)
				break
			elif block.intersectX(self):
				self.bounceX()
				blocks.remove(block)
				break
			elif block.intersectY(self):
				self.bounceY()
				blocks.remove(block)
				break

		if player.intersectX(self):
			self.bounceX()
		elif player.intersectY(self):
			self.bounceY()
	
	def bounceX(self):
		self.x -= self.xSpeed
		self.xSpeed *= -1

	def bounceY(self):
		self.y -= self.ySpeed
		self.ySpeed *= -1
import pygame

class Player:
	def __init__(self, displayWidth, displayHeight):
		self.sprite = pygame.image.load('./Sprites/playerRed.png') 
		self.height = self.sprite.get_height()
		self.width = self.sprite.get_width()
		self.x = displayWidth * 0.1
		self.y = displayHeight * 0.45
		self.displayWidth = displayWidth
		self.displayHeight = displayHeight
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
					self.ySpeed += -5
					self.up = True
				elif event.key == pygame.K_DOWN and self.down == False:
					self.ySpeed += 5
					self.down = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.ySpeed += 5
					self.up = False
				elif event.key == pygame.K_DOWN:
					self.ySpeed += -5
					self.down = False

		if self.y + self.ySpeed > self.displayHeight - self.height:
			self.y = self.displayHeight - self.height
		elif self.y + self.ySpeed < 0:
			self.y = 0
		else:
			self.y += self.ySpeed
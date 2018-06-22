import pygame

class Rect:
	def __init__(self, x, y, spriteFile):
		self.sprite = pygame.image.load(spriteFile)
		self.x = x
		self.y = y
		self.height = self.sprite.get_height()
		self.width = self.sprite.get_width()

	#only works for otherRects that are smaller than self, TODO: update that
	def intersect(self, otherRect):
		return ((otherRect.x > self.x and
			otherRect.x < self.x + self.width and
			otherRect.y > self.y and
			otherRect.y < self.y + self.height) or
			(otherRect.x + otherRect.width > self.x and
			otherRect.x + otherRect.width < self.x + self.width and
			otherRect.y > self.y and
			otherRect.y < self.y + self.height) or
			(otherRect.x + otherRect.width > self.x and
			otherRect.x + otherRect.width < self.x + self.width and
			otherRect.y + otherRect.height > self.y and
			otherRect.y + otherRect.height < self.y + self.height) or
			(otherRect.x > self.x and
			otherRect.x < self.x + self.width and
			otherRect.y + otherRect.height > self.y and
			otherRect.y + otherRect.height < self.y + self.height))

	def intersectX(self, otherRect):
		if self.intersect(otherRect):
			return abs(otherRect.x - self.x) > abs(otherRect.y - self.y)

	def intersectY(self, otherRect):
		if self.intersect(otherRect):
			return abs(otherRect.x - self.x) < abs(otherRect.y - self.y)

	def intersectBoth(self, otherRect):
		if self.intersect(otherRect):
			return abs(otherRect.x - self.x) == abs(otherRect.y - self.y)
import pygame

class Rect:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.height = h
		self.width = w

	def intersect(self, otherRect):
		return  (
				not otherRect.x > self.x + self.width and not
				otherRect.x + otherRect.width < self.x and not
				otherRect.y > self.y + self.height and not
				otherRect.y + otherRect.height < self.y
			)

	def intersectX(self, otherRect):
		if self.intersect(otherRect):
			#fix this later!
			if self.y < otherRect.y < otherRect.y + otherRect.height < self.y + self.height:
				return True
			return abs(otherRect.x - self.x) % otherRect.width > abs(otherRect.y - self.y) % otherRect.height

	def intersectY(self, otherRect):
		if self.intersect(otherRect):
			return abs(otherRect.x - self.x) % otherRect.width < abs(otherRect.y - self.y) % otherRect.height

	def intersectBoth(self, otherRect):
		if self.intersect(otherRect):
			return abs(otherRect.x - self.x) % otherRect.width == abs(otherRect.y - self.y) % otherRect.height
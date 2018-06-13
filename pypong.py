#!/usr/bin/env python3

import pygame
import modules.player as player
import modules.ball as ball

displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)
grey = (120,120,120)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Pypong')
clock = pygame.time.Clock()

playerObject = player.Player(displayWidth, displayHeight)
ballObject = ball.Ball(displayWidth, displayHeight)

def updateObjects():
	for item in gameElements:
		item.update()

def blitObjects():
	for item in gameElements:
		print(item, item.x, item.y)
		gameDisplay.blit(item.sprite, (item.x, item.y))

def gameLoop():
	gameExit = False
	while not gameExit:
		gameDisplay.fill(white)
		updateObjects()
		blitObjects()
		pygame.display.flip()
		clock.tick(60)

gameElements = [playerObject, ballObject]
gameLoop()
#quitting can be found in the player class (event handling)
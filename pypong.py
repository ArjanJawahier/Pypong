#!/usr/bin/env python3

import pygame
import modules.player as player
import modules.ball as ball
import modules.block as block

displayWidth = 800
displayHeight = 600
blockRows = 30
blockColumns = 20

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

playerObject = player.Player(displayWidth*0.1, displayHeight*0.45, './Sprites/playerRed.png', displayWidth, displayHeight)
ballObject = ball.Ball(displayWidth, displayHeight)
gameElements = [playerObject, ballObject]
gameBlocks = []

def generateBlocks():
	for i in range(0,blockRows):
		for j in range(0, blockColumns):
			blockX = 0.5*displayWidth + 17*j
			blockY = 0.1*displayHeight + 17*i
			gameBlocks.append(block.Block(blockX, blockY, './Sprites/ball.png'))

def updateObjects():
	playerObject.update()
	ballObject.update(gameBlocks, playerObject)

def blitObjects():
	for item in gameElements:
		gameDisplay.blit(item.sprite, (item.x, item.y))
	for block in gameBlocks:
		gameDisplay.blit(block.sprite, (block.x, block.y))

def gameLoop():
	gameExit = False
	while not gameExit:
		gameDisplay.fill(black)
		updateObjects()
		blitObjects()
		pygame.display.flip()
		clock.tick(60)

generateBlocks()
gameLoop()
#quitting can be found in the player class (event handling)
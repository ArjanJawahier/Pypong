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
			gameBlocks.append(block.Block(blockX, blockY, 16, 16))

def updateObjects():
	playerObject.update()
	ballObject.update(gameBlocks, playerObject)

def blitObjects():
	for item in gameElements:
		gameDisplay.blit(item.sprite, (item.x, item.y))
	for block in gameBlocks:
		pygame.draw.rect(gameDisplay, block.color, (block.x, block.y, block.width, block.height))

def createText(text, fontSize, color, centerX, centerY):
	font = pygame.font.SysFont("comicsansms", fontSize)
	textSurface = font.render(text, True, color)
	textRect = textSurface.get_rect()
	textRect.center = (centerX, centerY)
	gameDisplay.blit(textSurface, textRect)

def gameIntro():
	intro = True

	redness = 255
	blueness = 0
	redDecrease = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				intro = False

		gameDisplay.fill(black)
		if redDecrease:
			redness -= 1
			blueness += 1
		else:
			redness += 1
			blueness -= 1
		if redness == 0:
			redDecrease = False
		elif redness == 255:
			redDecrease = True
		textCol = (redness, 0, blueness) #starts at red and fades to blue and back
		createText("PYPONG", int(abs(redness-blueness)/2 + 10), textCol, displayWidth*0.5, displayHeight*0.5)
		createText("press any key to continue", 32, textCol, displayWidth*0.5, displayHeight*0.8)
		pygame.display.update()
		clock.tick(30)

def gameLoop():
	gameExit = False
	numBlocks = len(gameBlocks)
	while not gameExit:
		score = numBlocks - len(gameBlocks) - ballObject.timesHitLeftSide
		gameDisplay.fill(black)
		createText("Score: " + str(score), 22, white, displayWidth*0.05, displayHeight*0.05)
		updateObjects()
		blitObjects()
		pygame.display.flip()
		clock.tick(60)

gameIntro()
generateBlocks()
gameLoop()
#quitting can be found in the player class (event handling)
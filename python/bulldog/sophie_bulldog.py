import pygame
from pygame.locals import *
import sys
import random
# Creating a tuple to hold the RGB (Red, Green Blue) values
# So that we can paint our screen blue later
# And our text red
colorBLUE = (0, 0, 255)
colorRED = (255, 0, 0)
colorPINK = (255,200,200)
colorGREEN = (0,255,0)
colorBLACK = (0,0,0)
colorWHITE = (255,255,255)
colorYELLOW = (255,255,0)

# Initialize all of the Pygame modules so we can use them later on
pygame.init()
# Create the game screen and set it to 800 x 600 pixels
screen = pygame.display.set_mode((800, 600), 0, 32)
# Set a caption to our window
pygame.display.set_caption("Sophie the Bulldog!")
# Draw a blue background onto our screen/window
screen.fill(colorBLUE)

# Prepare our font for text
myFont = pygame.font.SysFont('None', 40)
# Create a text object
firstText = myFont.render("Sophie The Bulldog", True, colorRED, colorBLUE)
# Create the surface to write our text onto and its position
firstTextRect = firstText.get_rect()
firstTextRect.left = 100
firstTextRect.top = 75
# blit our text to the window
screen.blit(firstText, firstTextRect)

sidekick = pygame.Rect(150,150,200,200)
sophie = pygame.image.load('python/bulldog/bulldog.jpg')
thumbnail_sophie = pygame.transform.scale(sophie, (300,200))
screen.blit(thumbnail_sophie, sidekick)

# Drawing a circle
pygame.draw.circle(screen, colorRED, (330, 475), 15, 1)
pygame.draw.circle(screen, colorYELLOW, (375, 475), 15, 15)
pygame.draw.circle(screen, colorPINK, (420, 475), 20, 10)
pygame.draw.rect(screen, colorYELLOW, (455, 470, 20, 20), 4)
pygame.draw.line(screen, colorRED, (300, 500), (500,500),1)
pygame.draw.line(screen, colorYELLOW, (300, 515), (500,515),1)
pygame.draw.line(screen, colorRED, (300, 530), (500,530),1)

# Draw the now blue window to the screen
pygame.display.update()
# Create a variable to hold the value of whether the game should end or not
running = True
# Create a loop that will keep the game running
# Until the user decides to quit
# When they do, it will change the value of running
# To False, ending the game
while True:
# Get feedback from the player in the form of events
    for event in pygame.event.get():
# If the player clicks the red 'x', it is considered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                barkText = myFont.render("Bark!", True, colorRED, colorBLUE)
                barkTextRect = barkText.get_rect()
                barkTextRect.left = 450
                barkTextRect.top = 175
                screen.blit(barkText, barkTextRect)
                pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_b:
                barkText = myFont.render("Bark!", True, colorBLUE, colorBLUE)
                barkTextRect = barkText.get_rect()
                barkTextRect.left = 450
                barkTextRect.top = 175
                screen.blit(barkText, barkTextRect)
                pygame.display.update()

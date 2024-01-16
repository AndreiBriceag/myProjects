import pygame
from pygame.locals import *
import sys
# Initialize all of the Pygame modules so we can use them later on
pygame.init()
# Create the game screen and set it to 800 x 600 pixels
screen = pygame.display.set_mode((800, 600))
# Create a loop that will keep the game running
# Until the user decides to quit
while True:
# Get feedback from the player in the form of events
    for event in pygame.event.get():
# If the player clicks the red 'x', it is considered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

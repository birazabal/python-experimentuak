https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python

# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys=[False, False, False, False]
jokalaripos=[100,100]
maltzurrapos=[440,100]	
# 3 - Load images
jokalaria = pygame.image.load("/home/galtzagorri/Mahaigaina/hiperkuak.png")
maltzurra = pygame.image.load("/home/galtzagorri/Mahaigaina/maltzurra.png")
fondua = pygame.image.load("/home/galtzagorri/Mahaigaina/hiperkuakfondua.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(fondua, (0,0))
    screen.blit(jokalaria, jokalaripos)
    screen.blit(maltzurra, maltzurrapos)
    # 7 - update the screen
    pygame.display.flip()
    maltzurrapos[0]-=1 
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
        # 9 - Move player
        if keys[0]:
            jokalaripos[1]-=5
        elif keys[2]:
            jokalaripos[1]+=5
        if keys[1]:
            jokalaripos[0]-=5
        elif keys[3]:
            jokalaripos[0]+=5
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()

import pygame
from pygame.locals import *
from sys import exit
import sys

startPics = {'bg': pygame.image.load('startBG3.png'),
             'mascot':pygame.image.load('mascotStart-01.png'),
             'bubble':pygame.image.load('balloon.png')}




class Start(object):
    def __init__(self, screen):
        self._screen = screen
        
    def startScreen(self):
        """shows a start up screen"""
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        TEXTCOLOR = (255, 255, 255)
        topCoord = 500
        HALF_WINWIDTH = (665)//2
        self._screen.blit(startPics['bg'],(0,0))

        instructionText = ['Arrow keys to move',
                            'Collect electronic wastes',
                            'Reach the goal point to go to next level',
                            '',
                            '[Press any key to continue...]'] 

        for i in range(len(instructionText)):
             instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
             instRect = instSurf.get_rect()
             topCoord += 10 # 10 pixels will go in between each line of text.
             instRect.top = topCoord
             instRect.centerx = HALF_WINWIDTH
             topCoord += instRect.height # Adjust for the height of the line.
             self._screen.blit(instSurf, instRect) 

        while True: # Main loop for the start screen.
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:
                    if event.type == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    return # user has pressed a key, so return.
                
                    
            #Display the DISPLAYSURF contents to the actual screen.
            pygame.display.update()

    def startScreen2(self):
        
        self._screen.blit(startPics['bg'],(0,0))
        self._screen.blit(startPics['mascot'],(0,0))
        self._screen.blit(startPics['bubble'],(0,0))
        

        instructionText = ['Arrow keys to move',
                            'Collect electronic wastes',
                            'Reach the goal point to go to next level',
                            '',
                            '[Press any key to continue...]'] 

        while True: # Main loop for the start screen.
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == KEYDOWN:
                    if event.type == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    return # user has pressed a key, so return.
                
                    
            #Display the DISPLAYSURF contents to the actual screen.
            pygame.display.update()


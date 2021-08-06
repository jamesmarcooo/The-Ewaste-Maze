import pygame
from pygame.locals import *
import sys

class Control(object):
    def __init__(self, dx,dy,dx2,dy2, bouncerate,SCALED):
        self._dx = 1*35
        self._dy = 1*35
        self._dx2 = dx2
        self._dy2 = dy2
        self._bouncerate = bouncerate
        self._moveUp = True
        self._moveDown = False
        self._space = False
        self._SCALED = SCALED
        self._facing = self._SCALED['spriteR']

    def eventControl(self):
        """this set the speed of the sprite"""
        for event in pygame.event.get(): #returns a sequence type na nandun yung state ng pygame window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN: #unpressed -> pressed will call KEYDOWN .... pressed -> unpressed KEYUP
                if event.key == K_ESCAPE: #pressed ESC
                    pygame.quit()
                    sys.exit() 


                #to face Up
                elif event.key == K_RIGHT and self._facing == self._SCALED['spriteL']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteU']
                elif event.key == K_LEFT and self._facing == self._SCALED['spriteR']:
                    self._moveUp = True
                    self._facing = self._SCALED['spriteU']

                #to face down    
                elif event.key == K_RIGHT and self._facing == self._SCALED['spriteR']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteD']
                elif event.key == K_LEFT and self._facing == self._SCALED['spriteL']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteD']

                #to face right   
                elif event.key == K_RIGHT and self._facing == self._SCALED['spriteU']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteR']
                elif event.key == K_RIGHT and self._facing == self._SCALED['spriteD']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteR']

                #to face left         
                elif event.key == K_LEFT and self._facing == self._SCALED['spriteD']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteL']
                elif event.key == K_LEFT and self._facing == self._SCALED['spriteU']:
                    self._moveUp = True
                    self._moveDown = False
                    self._facing = self._SCALED['spriteL']

                #to stop 
                elif event.key == K_SPACE:
                    self._moveUp = False
                    self._moveDown = False
                    self._dy2 = 0
                    self._dx2 = 0
                #decelerate
                elif event.key == K_DOWN:
                    self._moveDown = True
                    self._moveUp = False

                elif event.key == K_UP:
                    self._moveDown = False
                    self._moveUp = True
                    
                """                   
                elif event.key == K_DOWN: #arrowdown key
                    self._moveDown = True
                    self._moveUp = False
                    self._facing = self._SCALED['spriteD']
                elif event.key == K_UP and self._facing != self._SCALED['spriteU']: #arrowup key
                    self._moveDown = False
                    self._moveUp = True
                    self._facing = self._SCALED['spriteU']
                elif event.key == K_LEFT: #arrowleft key
                    self._moveRight = False
                    self._moveLeft = True
                    self._facing = self._SCALED['spriteL']
                elif event.key == K_RIGHT: #arrowup key
                    self._moveLeft = False
                    self._moveRight = True
                    self._facing = self._SCALED['spriteR']
                elif event.key == K_SPACE:
                    self._dy2 = 0
                    self._dx2 = 0
                else:
                    self._moveUp = True
                    self._facing = self._SCALED['spriteU']
                """    

            elif event.type == KEYUP: #pressed -> unpressed will call KEYUP
                if event.key == K_SPACE: #arrowdown key
                    #self._space = False
                    self._moveUp = True
                
                    
            """        
            elif event.type == KEYUP: #pressed -> unpressed will call KEYUP
                if event.key == K_DOWN: #arrowdown key
                    self._dy2 = 0
                    self._moveDown = False
                elif event.key == K_UP: #arrowup key
                    self._dy2 = 0
                    self._moveUp = False
                elif event.key == K_LEFT: #arrowleft key
                    self._dx2 = 0
                    self._moveLeft = False
                elif event.key == K_RIGHT: #arrowup key
                    self._dx2 = 0
                    self._moveLeft = False
            """

            #to accelerate and decelerate
            if self._moveUp and self._facing == self._SCALED['spriteR']:
                self._dx2 += 2
                self._dy2 = 0
            elif self._moveDown and self._facing == self._SCALED['spriteU']:
                self._dx2 += -2
                self._dy2 = 0
            
            if self._moveUp and self._facing == self._SCALED['spriteL']:
                self._dx2 += -2
                self._dy2 = 0
            elif self._moveDown and self._facing == self._SCALED['spriteL']:
                self._dx2 += 2
                self._dy2 = 0
            
                
            if self._moveUp and self._facing == self._SCALED['spriteU']:
                self._dx2 = 0
                self._dy2 += -2
            elif self._moveDown and self._facing == self._SCALED['spriteU']:
                self._dx2 = 0
                self._dy2 += 2
                
            if self._moveUp and self._facing == self._SCALED['spriteD']:
                self._dx2 = 0
                self._dy2 += 2
            elif self._moveDown and self._facing == self._SCALED['spriteD']:
                self._dx2 = 0
                self._dy2 += -2

            
                
            
        #self._dx += self._dx2
        #self._dy += self._dy2

        return self._dx2, self._dy2, self._bouncerate, self._facing
        

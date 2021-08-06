import pygame
import math
from gridview import GridView
from maze_randomizer import RandomMaze
from path_finder import MazePathFinder
from controlEvents import Control
from startScreen import Start
import pygame
from pygame.locals import *
from sys import exit
import sys
import random


class Game(object):
        def __init__(self, reso, width, height, grid_size, grid_line_color, background_color, cell_color, IMAGES, SCALED):
                self._resolution = reso
                self._width = width
                self._height = height
                self._grid_size = grid_size
                self._grid_line_color = grid_line_color
                self._background_color = background_color
                self._cell_color = cell_color
                self._speed = 0.010
                self._mode = 0
                
                self._BOUNCERATE = 6
                self._BOUNCEHEIGHT = 15
                self._IMAGES = IMAGES
                self._SCALED = SCALED
                self._itemList = []
                self._ctr = 0
                self._facing = self._SCALED['spriteR']
                self._wallList = []
                self._wallObj= 0
                self._itemsList = []
                self._itemsObj = 0

                self._points = 0

        def runGame(self, maze_method):
                """the main function of the game"""
                global IMAGES
                endx = 0
                endy = 0
                screen = pygame.display.set_mode(self._resolution, 0, 32)
                clock = pygame.time.Clock()
                maze, cell_list = maze_method()


                #START
                start = Start(screen)
                start.startScreen()
                start.startScreen2()
                
                print(maze)
                
                #For the initial speed
                speedx2 = 0
                speedy2 = 0


                index = 0
                path_index = 0
                maze_finished = False

                pass_time = 0
                grid_view = GridView(screen, self._width, self._height, self._grid_size, self._grid_line_color)

                playerObj = {'x':1*35,
                             'y':1*35,
                             'x2':0,
                             'y2':0,
                             'bounce':0,
                             #'health': MAXHEALTH
                             }
                
                occupiedPos = []
                randomGenSpritePos = 0                

                eventHandle = Control(playerObj['x'],playerObj['y'],playerObj['x2'],playerObj['y2'],playerObj['bounce'],self._SCALED)
                
                while True:
                        press_key = pygame.key.get_pressed()
                        
                        if playerObj['x'] == endx and playerObj['y'] == endy:
                                index = 0
                                path_index = 0
                                self._ctr = 0
                                del self._itemList[:]
                                maze, cell_list = maze_method()
                                #path_finder = MazePathFinder(maze, (2, 2), (cell_row_num * 2, cell_col_num * 2), 
                                #        height//grid_size, width//grid_size)
                                #path = path_finder.bfs_find_path()
                                maze_finished = False

                                if self._ctr <= 20:
                                        randomGenItemPos = random.choice(self.randLoc(maze))
                                        ewaste = random.choice(items)
                                        self._itemList.append((ewaste,randomGenItemPos))
                                        self._ctr +=1

                        #initial position
                        
                        
                        """
                        # press F5 to regenerate the maze
                        if press_key[K_F5]:
                                index = 0
                                path_index = 0
                                maze, cell_list = maze_method()
                                path_finder = MazePathFinder(maze, (2, 2), (cell_row_num * 2, cell_col_num * 2), 
                                        height//grid_size, width//grid_size)
                                path = path_finder.bfs_find_path()
                                maze_finished = False
                        """
                        #print (index)

                        if self._mode == 0:
                                #screen.fill((255,255,255))
                                screen.blit(self._IMAGES['bgfill'], (-200,0))
                        else:
                                screen.fill(self._cell_color)

                        # draw the grid
                        #grid_view.draw()
                        

                        """
                        # draw the cell
                        for i in range(index + 1):
                                if self._mode == 0:
                                        #grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], self._cell_color)
                                        for coord in i
                                        screen.blit(self._IMAGES['wall'], cell_list[index])

                                else:
                                    grid_view.fill_a_cell(cell_list[i][1], cell_list[i][0], self._background_color)
                        """

                        
                        time_passed_seconds = clock.tick() / 1000.0
                        pass_time += time_passed_seconds
                        
                        
                        if pass_time >= self._speed:
                                pass_time = 0
                                #if maze_finished:
                                        #if path_index + 1 < len(path):
                                         #       path_index += 1

                                if index >= len(cell_list) - 1:
                                        #print('maze_finished')
                                        maze_finished = True
                                        
                                if index + 1 < len(cell_list):
                                        index += 1
                                        
                        
                        
                        #import picWall
                        for row in range(len(maze)):
                               for col in range(len(maze[row])):
                                       if maze[row][col] == 0:
                                               screen.blit(self._IMAGES['wallD'], (row*self._grid_size,col*self._grid_size-7.5))
                        
                        #Drawing of items randomly
                        items = [self._SCALED['item1'],self._SCALED['item3'],self._SCALED['item4'], self._SCALED['enemy']]
                        if self._ctr <= 20:
                                randomGenItemPos = random.choice(self.randLoc(maze))
                                occupiedPos.append(randomGenItemPos)
                                ewaste = random.choice(items)
                                if (ewaste,randomGenItemPos) not in self._itemList:
                                        self._itemList.append((ewaste,randomGenItemPos))
                                        self._ctr +=1

                        for i,p in self._itemList:
                                screen.blit(i,p)
                                row,col = p
                                self._itemsList.append(self.createItems(row,col))

                        

                        #Random position of Sprite
                        if self._ctr == 1:
                                randomGenSpritePos = random.choice(self.randLoc(maze))
                                if randomGenSpritePos not in occupiedPos:
                                        playerObj['x'], playerObj['y']  = randomGenSpritePos
                                        

                        if self._ctr == 2:
                                randomGenEndPos = random.choice(self.randLoc(maze))
                                if randomGenEndPos not in occupiedPos:
                                        endx, endy  = randomGenEndPos
                                                 

                        #drawing of End
                        playerObj['end'] = pygame.Rect( (endx, endy, 30,30))
                        screen.blit(self._SCALED['end'], playerObj['end'])
                        
                        #drawing of Sprite
                        playerObj['rect'] = pygame.Rect( (playerObj['x'], playerObj['y'], 30,30))
                        screen.blit(self._facing, playerObj['rect'])

                        #drawing of Wall
                        for row in range(len(maze)):
                               for col in range(len(maze[row])):
                                        if maze[row][col] == 0:
                                                       screen.blit(self._IMAGES['wallU'], (row*self._grid_size,col*self._grid_size-4))
                                                       self._wallList.append(self.createWall(row,col))
                                        
                                                
                        
                        #Collision Detection 
                        objwall = 0
                        collisionctr= 0
                        for i in range(len(self._wallList)-1, -1, -1): 
                                objwall = self._wallList[i]
                                if 'rect' in objwall and (playerObj['rect'].colliderect(objwall['rect'])):
                                        collisionctr += 1
                                        break

                        objitems = 0
                        for i in range(len(self._itemsList)-1, -1, -1): 
                                objitems = self._itemsList[i]
                                if 'rect' in objitems and (playerObj['rect'].colliderect(objitems['rect'])):
                                        print(playerObj['rect'].colliderect(objitems['rect']))
                                        break

                        
                                        
                        #Collision Avoidance
                        if collisionctr >= 1:          
                                playerObj['x2'] = -playerObj['x2']
                                playerObj['y2'] = -playerObj['y2']
                        else:
                                playerObj['x2'],playerObj['y2'], playerObj['bounce'],self._facing = eventHandle.eventControl()

                        #Speed of Sprite
                        playerObj['x'] += playerObj['x2']
                        playerObj['y'] += playerObj['y2']

                        
                        
                        
                        pygame.display.update()


        def randLoc(self, maze):
                """returns a list of x and y position"""
                lis = []
                #print(maze)
                
                for rows in range(len(maze)):
                        for cols in range(len(maze[rows])):
                                if maze[rows][cols] == 1:
                                        lis.append((rows*self._grid_size, cols*self._grid_size))
                                        

                return lis
        
        def createWall(self, row, col):
                """returns a dictionary intended for each wall object"""
                wallObj = {}
                wallObj['rect'] =pygame.Rect(row*self._grid_size,col*self._grid_size,self._grid_size,self._grid_size)
                
                return wallObj

        def createItems(self, row, col):
                """returns a dictionary intended for each item object"""
                itemsObj = {}
                itemsObj['rect'] =pygame.Rect(row*self._grid_size,col*self._grid_size,30,30)
                
                return itemsObj        
                
        
        def parser_arg(self, argv):
                """
                parser the arguments,
                python main.py [OPTION]:
                        -d --dfs: use dfs algorithm to generate the maze, and return 1(default value)
                        -k --kruscal: use kruscal algorithm to generate the maze, and return 2
                """
                args = argv[1:]
                if len(args) == 0:
                        return 1
                elif len(args) > 1:
                        print('Error option')
                        print('Usage:')
                        print("(python) main.py [OPTION]: \n" + \
                        "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                        "  -k --kruscal: use kruscal algorithm to generate the maze ")
                        return 0
                elif args[0] == '-d' or args[0] == '--dfs':
                        return 1
                elif args[0] == '-k' or args[0] == '--kruscal':
                        return 2
                else:
                        print('Error option')
                        print('Usage:')
                        print("(python) main.py [OPTION]: \n" + \
                        "  -d --dfs: use dfs algorithm to generate the maze(default option)\n" +\
                        "  -k --kruscal: use kruscal algorithm to generate the maze ")
                        return 0



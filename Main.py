from runthegame import Game
from maze_randomizer import RandomMaze
from startScreen import Start
import pygame
from pygame.locals import *
from sys import exit
import sys



def get_maze_method(option):

    
    if option == 1:
        return ran_maze.dfs_maze
    elif option == 2:
        return ran_maze.disjoint_make_maze
    else:
        return None

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

width = 665
height = 665
grid_size = 35

background_color = (230, 230, 100)
grid_line_color = (0, 0, 0)
cell_color = (50, 50, 255)
path_color = (255, 50, 50)

resolution = (width, height)

ran_maze = RandomMaze(width//grid_size, height//grid_size)

cell_row_num = (height//grid_size - 3) // 2
cell_col_num = (width//grid_size - 3) // 2

IMAGES =  {'spriteL': pygame.image.load('teppyL-01.png'),
           'spriteR': pygame.image.load('teppyR-01.png'),
           'spriteD': pygame.image.load('teppyF-01.png'),
           'spriteU': pygame.image.load('teppyB-01.png'),
           'wallU': pygame.image.load('wallgrassUP2.png'),
           'wallD': pygame.image.load('wallgrassDOWN.png'),
           'bgfill':pygame.image.load('bgfill3-01.png'),
           'item1': pygame.image.load('item-laptop.png'),
           'item3': pygame.image.load('item-CPU.png'),
           'item4': pygame.image.load('item-vidcam.png'),
           'enemy': pygame.image.load('ENEMYFIRE-01.png'),
           'end': pygame.image.load('End.png')
           }

SCALED = {'spriteL':(pygame.transform.scale(IMAGES['spriteL'], (30, 30))),
          'spriteR':(pygame.transform.scale(IMAGES['spriteR'], (30, 30))),
          'spriteD':(pygame.transform.scale(IMAGES['spriteD'], (30, 30))),
          'spriteU':(pygame.transform.scale(IMAGES['spriteU'], (30, 30))),
          'item1':(pygame.transform.scale(IMAGES['item1'], (30,30))),
          'item3':(pygame.transform.scale(IMAGES['item3'], (30,30))),
          'item4':(pygame.transform.scale(IMAGES['item4'], (30,30))),
          'enemy':(pygame.transform.scale(IMAGES['enemy'], (30,30))),
          'end':(pygame.transform.scale(IMAGES['end'], (30,30)))}
        



run = Game(resolution, width, height, grid_size, grid_line_color, background_color, cell_color,IMAGES,SCALED) #Instantiate the Game class (main game code)



while True:
    method = get_maze_method(run.parser_arg(sys.argv))
    if method:
        run.runGame(maze_method = get_maze_method(run.parser_arg(sys.argv)))
     


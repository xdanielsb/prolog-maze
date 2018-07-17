import pygame
from pygame.locals import *

def drawSol(maze, ROWS, COLS):
  aux=0;
  pygame.init()
  w=pygame.display.set_mode((900,600))
  pygame.display.set_caption("Maze")

  root = 'assets/'
  imgStart = pygame.image.load(root+"door.png")
  imgBusy = pygame.image.load(root+"wall.png")
  imgFree = pygame.image.load(root+"footprint.png")
  imgEnd = pygame.image.load(root+"treasure.png")
  imgWay = pygame.image.load(root+"foot.png")
  imgBack = pygame.image.load(root+"fondo2.png")
  
  w.blit(imgBack,(0,0))
  
  S = 200
  for r in range(ROWS):
    for j in range( COLS):
      pos = (j*64+S, r*64+S)
      try:
        if maze[r][j] =='S':   w.blit(imgStart, pos)
        elif maze[r][j] =='1': w.blit(imgBusy, pos)
        elif maze[r][j] =='0': w.blit(imgFree, pos)
        elif maze[r][j] =='E': w.blit(imgEnd, pos)
        elif maze[r][j] =='X': w.blit(imgWay, pos)
      except IndexError:
        pass

  pygame.display.flip()
  while True:
    for eventos in pygame.event.get():
      if eventos.type==pygame.QUIT:
        sys.exit(0)



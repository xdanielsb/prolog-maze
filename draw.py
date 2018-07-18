import pygame
from pygame.locals import *

def drawSol(maze, ROWS, COLS):
  aux=0;
  pygame.init()
  w=pygame.display.set_mode((900,600))
  pygame.display.set_caption("Maze")

  root = 'assets/'
  images = {} 
  images['S'] = pygame.image.load(root+"door.png")
  images['1'] = pygame.image.load(root+"wall.png")
  images['0'] = pygame.image.load(root+"footprint.png")
  images['E'] = pygame.image.load(root+"treasure.png")
  images['X'] = pygame.image.load(root+"foot.png")
  imgBack = pygame.image.load(root+"fondo2.png")
  
  w.blit(imgBack,(0,0))
  
  S = 200
  for r in range(ROWS):
    for j in range( COLS):
      pos = (j*64+S, r*64+S)
      idx = maze[r][j]
      try:
        w.blit(images[idx], pos)
      except IndexError:
        print(" E01 = {}".format("Error in pos"))

  pygame.display.flip()
  while True:
    for eventos in pygame.event.get():
      if eventos.type==pygame.QUIT:
        sys.exit(0)



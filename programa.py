from __future__ import print_function
from pyswip import Prolog, Functor, Variable, Query
import random
import pygame
from pygame.locals import *
import sys

maze = []
ways =[]
vis =[]
inm =[]
outm = []
ROWS, COLS = 0, 0

p = Prolog()

#load map
def load( f ):
  for col in f:
    row = []
    for item in col[:-2]:
      row.append( item) 
    maze.append(row)

#find in out
def find():
  global ROWS, COLS
  ROWS = len( maze )
  COLS = len( maze[0] )
  for r in range(ROWS):
    for c in range(COLS):
      if maze[r][c] == 'E':
        inm.append([str(r),str(c)])
      elif maze[r][c] =='S':
        outm.append([str(r),str(c)])

#create paths 
def create(ra, rc, r , c ):
  if  c >= ROWS or r >= ROWS: return
  if  r < 0 or c < 0: return
  if (ra, rc, r,c)  in vis: return
  if (r, c, ra, rc) in vis: return;
  vis.append((ra, rc, r,c))
  if(ra == r and rc == c ): return
  if  maze[r][c] == '1': return
  ways.append([ra, rc, r , c])
  create(r , c, r-1, c)
  create(r , c, r, c-1)
  create(r , c, r+1, c)
  create(r , c, r, c+1)

#print maze
def printm():
  for row in maze:
    for it in row:
      print(it, end=" ")
    print()

def solveProlog():
  p.consult('prolog/solve.pl')
  q = "ir({},{},X)".format(inm[0], outm[0])
  res = []
  try:
    for  r in  p.query(q):
      path = r["X"]
      for a in path[1:-1]:
        tu = [a[0].value, a[1].value]
        res.append(tu)
        tu = [ int(x) for x in tu]
        maze[tu[0]][tu[1]] ='X'
      a = path[(len(path)-1)]
      return res
  except Exception as e:
    print( "ex", e)
 
def dibujar():
  aux=0;
  pygame.init()
  w=pygame.display.set_mode((900,600))
  pygame.display.set_caption("Laberinto")

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
        if maze[r][j] =='S':
          w.blit(imgStart, pos)
        elif maze[r][j] =='1':
          w.blit(imgBusy, pos)
        elif maze[r][j] =='0':
          w.blit(imgFree, pos)
        elif maze[r][j] =='E':
          w.blit(imgEnd, pos)
        elif maze[r][j] =='X':
          w.blit(imgWay, pos)
      except IndexError:
        pass

  pygame.display.flip()
  while True:
    for eventos in pygame.event.get():
      if eventos.type==pygame.QUIT:
        sys.exit(0)

if __name__ == "__main__":
  
  #load the map
  load( open('maze-conf') )
  #find the in and out
  find( )
  #create the paths for the facts in Prolog
  x , y = int(inm[0][0]), int(inm[0][1])
  create(x, y+1, x, y)
  random.shuffle( ways )
  fipl =open("prolog/solve.pl","w")
  for li in ways[1:]:
    way = "calle('{}','{}','{}','{}').\n".format(li[0],li[1], li[2], li[3])
    fipl.write( way )

  q = open("prolog/query.pl")
  fipl.write(q.read())
  q.close()
  fipl.close()

  print("Original Maze")
  printm()
  path = solveProlog()
  print("Solve maze")
  printm()
  dibujar()








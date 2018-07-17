from __future__ import print_function
from pyswip import Prolog, Functor, Variable, Query
from draw import drawSol
import random
import sys


maze = []
ways =[]
vis =[]
inm =[]
outm = []
ROWS, COLS = 0, 0

p = Prolog()

def load( f ):
  for col in f:
    maze.append( [i for i in col[:-2]]) 

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

#Create the facts for prolog
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

if __name__ == "__main__":
  
  load( open('maze-conf') )
  find( )
  #create the paths for the facts in Prolog
  x , y = int(inm[0][0]), int(inm[0][1])
  create(x, y+1, x, y)
  
  random.shuffle( ways )
  fipl =open("prolog/solve.pl","w")
  for li in ways[1:]:
    way = "calle('{}','{}','{}','{}').\n".format(li[0],li[1], li[2], li[3])
    fipl.write( way )

  #Logic find path in prolog
  q = open("prolog/query.pl")
  fipl.write(q.read())
  q.close()
  fipl.close()

  print("Original Maze")
  printm()
  
  path = solveProlog() #here we go
  
  print("Solve maze")
  printm()

  drawSol(maze, ROWS, COLS)








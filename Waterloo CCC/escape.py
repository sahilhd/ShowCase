import math
from collections import defaultdict
from sys import setrecursionlimit,getrecursionlimit

steps = defaultdict(list)
postion = []

def nextstep(curv, row, col):
  i = 1
  while i * i <= curv:
    if curv % i == 0 and i <= max(row, col) and curv // i <= max(row,col):
      steps[curv].append(i)
    i += 1;
  return curv

def DepthFirstSearch(curI, curJ, nrow, ncol):
  if curI == nrow-1 and curj == ncol -1:
    return True
  if curI >= nrow or curJ >= ncol or postion[curI][curJ] in steps:
    return False
  nextdest = nextstep(postion[curI][curK], nrow , ncol)
  for newI in steps[nextdest]:
    newJ = nextdest // newI
    if DepthFirstSearch(NewI -1 , newJ -1, nrow, ncol) or DepthFirstSearch( newJ -1,NewI -1 , nrow, ncol):
      return True
    return False

if __name__ == '__main__':
  setrecursionlimit(int(1e6 + 5))

  Ndimension = lambda : int(input())
  listn = lambda : list(map(int, input.split()))
  nrow, ncol = Ndimension , Ndimension
  for i in range(nrow):
    postion.append(listn())
  print('yes' if DepthFirstSearch(0,0, nrow,ncol) else 'no')



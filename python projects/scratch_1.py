import numpy as np

N = int(input())
M = int(input())
data = []
for m in range(M):
  row = list(map(int, input().split()))
  data.append(row)
arr = np.array(data)
def I_escape(value):
  locs = np.argwhere(arr == value)
  print(f'Locations: \n{locs}')
  for M,N in locs:
    if M ==0 and N == 0:
      return True
    else:
      if I_escape((M+1)*(N+1)):
        return True
  return False
end = N * M


if I_escape(end):
  print('yes')

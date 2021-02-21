number = input()
width = input()
length = input()
# (b1 * b2 /2)h
area = 0
counter = 0

width = width.split(' ')
length = length.split(' ')

while counter < int(number):
  area += 1
  int(width[counter])*(int(length[counter]) + int(length[counter + 1])) /2
  counter = counter + 1

print(area)
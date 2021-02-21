number = input()
length = input()
width = input()
# (b1 * b2 /2)h
area = 0
counter = 0

length = length.split(' ')
width = width.split(' ')



while counter < int(number):
  area += int(width[counter])*(int(length[counter]) + int(length[counter + 1])) /2
  counter = counter + 1

print(area)
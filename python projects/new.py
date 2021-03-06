N = int(input())
observations = []

for i in range(N):
  observation = {}
  line = input().split()
  observation['time'] = int(line[0])
  observation['pos'] = int(line[1])
  observations.append(observation)

def get_time(dict):
  return dict['time']
observations.sort(key = get_time)

max_speed = None
previous_time = None
previous_pos = None

for observation in observations:
  time = observation['time']
  pos = observation['pos']
  if previous_time == None:
    previous_time = time
    previous_pos = pos
    continue
  time_diff = time - previous_time
  distance = abs(pos - previous_pos)
  speed = distance / time_diff
  if max_speed == None or speed > max_speed:
    max_speed = speed
  previous_time = time
  previous_pos = pos
print(max_speed)


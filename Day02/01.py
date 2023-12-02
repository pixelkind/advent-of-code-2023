# 12 red cubes, 13 green cubes, and 14 blue cubes

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

max = {'red': 12, 'green': 13, 'blue': 14}

result = 0
def parse_game(game_string):
  global result
  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
  v = game_string.split(': ')
  id = v[0].split(' ')[1]
  # print(id)
  rounds = v[1].split('; ')
  possible = True
  for r in rounds:
    round = r.split(', ')
    for cubes_string in round:
      cubes = cubes_string.split(' ')
      if max[cubes[1]] < int(cubes[0]):
        possible = False
        break
  
  if possible:
    result += int(id)

for line in lines:
  parse_game(line)

print(result)
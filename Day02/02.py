file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

result = 0
def parse_game(game_string):
  global result
  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
  v = game_string.split(': ')
  rounds = v[1].split('; ')
  
  max_values = {'red': 0, 'green': 0, 'blue': 0}
  for r in rounds:
    round = r.split(', ')
    for cubes_string in round:
      cubes = cubes_string.split(' ')
      color = cubes[1]
      value = int(cubes[0])
      max_values[color] = max(max_values[color], value)
  
  result += max_values['red'] * max_values['blue'] * max_values['green']
  
for line in lines:
  parse_game(line)

print(result)
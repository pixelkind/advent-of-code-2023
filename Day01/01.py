file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")

result = 0
for line in lines:
  digits = list(filter(lambda s: s.isdigit(), line))
  nr = int(digits[0] + digits[-1])
  result += nr

print(result)
file = open('./input.txt', 'r')
string = file.read()
lines = string.split("\n")

digit_strings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

result = 0
for line in lines:
  found = {}
  for key in digits:
    start = 0
    while True:
      index = line.find(key, start)
      if index != -1:
        found[index] = key
        start = index + 1
      else:
        break
  
  sorted_dict = dict(sorted(found.items()))
  # print(sorted_dict)

  l = list(sorted_dict)
  # print(l[0], l[-1])
  first_element = sorted_dict[l[0]]
  if len(first_element) > 1:
    first_element = str(digit_strings[first_element])

  last_element = sorted_dict[l[-1]]
  if len(last_element) > 1:
    last_element = str(digit_strings[last_element])
  
  nr = int(first_element + last_element)
  # print(nr)
  result += nr

print(result)
data = []

with open('input.txt', 'r') as file:
  for x in file:
    data.append(file.readline())

print(data)
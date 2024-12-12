with open('input.txt', 'r') as file:
  lines = file.readlines()

column1 = []
column2 = []

for line in lines:
  left, right = line.split()  
  column1.append(int(left))  
  column2.append(int(right))  

column1.sort()
column2.sort()

diff = 0

for x, y in zip(column1, column2):
  diff += abs(x-y)
  
print(diff)








with open('input.txt', 'r') as file:
  lines = file.readlines()

column1 = []
column2 = []

for line in lines:
  left, right = line.split()  
  column1.append(int(left))  
  column2.append(int(right))  

score = 0

for x in column1:
  score += x * column2.count(x)

print(score)
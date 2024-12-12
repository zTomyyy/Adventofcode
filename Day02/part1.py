data = []
safes = 0
unsafes = 0


with open('input.txt', 'r') as file:
  for elements in file:
    datastr = elements.split()
    print(datastr)
    data = list(map(int, datastr))
    d = 0
    safe = True
    if data[0] < data[1]:
      d = 1
    before = data[0]
    for elements in data[1:]:
      if (before < elements and d == 0) or (before > elements and d == 1):
        safe = False
        print("Error - Steigung")
      if abs(before - elements) < 1 or abs(before - elements) > 3:
        safe = False
        print("Error - Differenz")
      before = elements
    print(safe)
    if safe == True:
      safes += 1
    if safe == False:
      unsafes += 1
    print("-----------------------------------")
  print(safes)
  print(unsafes)
  print(safes + unsafes)
   










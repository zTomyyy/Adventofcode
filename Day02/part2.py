#Function for checking if Safe (Returns T/F)
def check(data):
  # Ermitteln der Richtung (1: steigend, 0: fallend)
  d = 1 if data[0] < data[1] else 0
  safe = True

  for i in range(1, len(data)):
      diff = data[i] - data[i - 1]

      # Bedingung für steigende/fallende Zahlen
      if (diff > 0 and d == 0) or (diff < 0 and d == 1):
          return False  # Error: Reihenfolge

      # Bedingung für Differenzen
      if abs(diff) < 1 or abs(diff) > 3:
          return False  # Error: Differenz

  return True

def checkifdamper(data):
  index = 0
  copy = []
  for i in data:
    copy = data.copy()
    #print("Before removing:")
    #print(copy)
    del copy[index]
    #print("After removing:")
    #print(copy)
    if check(copy):
      return True
    index += 1
    #print("----------------")
  return False

#Read input data
data = []
with open('input.txt', 'r') as file:
  for elements in file:
    datastr = elements.split()
    data.append(list(map(int, datastr)))

print("Read data...")

unsafe = []

#check for safes

safecodes = 0
for i in data:
  if not check(i):
    unsafe.append(i)
  else:
    safecodes += 1

print("Safe codes found:")
print(safecodes)
print("Unsafe codes found:")
print(len(unsafe))

#check unsafe codes without elements
if len(unsafe) != 0:
  print("See if new safecodes can be found...")
  for i in unsafe:
    if(checkifdamper(i)):
      safecodes += 1
print("New Safecodes count:")
print(safecodes)

"""
data = []
safes = 0
unsafes = 0
unsafeelements = []

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
      unsafeelements.append(data)
    print("-----------------------------------")
  print("Safe:")
  print(safes)
  print("Unsafe:")
  print(unsafes)
  print("Elements")
  print(safes + unsafes)
  print("All unsafe Elements")
  print(unsafeelements)
  
  safies = 0

  for x in unsafeelements:   
    data = x
    datacopy = 0
    i = 0
    print("-------------------------")
    print("UNSAFE ELEMENT:")
    for y in data:
      datacopy = data.copy()
      print(datacopy)
      del datacopy[i]
      print(datacopy)
      safe = True
      print(i)
      i += 1
      if datacopy[0] < datacopy[1]:
        d = 1
      before = datacopy[0]
      for elements in datacopy[1:]:
        if (before < elements and d == 0) or (before > elements and d == 1):
          safe = False
          print("Error - Steigung")
        if abs(before - elements) < 1 or abs(before - elements) > 3:
          safe = False
          print("Error - Differenz")
        before = elements 
      print(safe) 
      if safe:
        safies += 1
    print("New Saves:")
    print(safies)
"""
      




   










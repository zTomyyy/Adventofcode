import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "input.txt")

# Datei einlesen
with open(file_path, "r") as file:
  lines = file.readlines()

rules = []
pages = []
check = True

for element in lines:
  if element != '\n' and check:
    rules.append(element)
  elif not check:
    pages.append(element)
  else:
    check = False

rules = [list(map(int, item.split('|'))) for item in rules]
pages = [list(map(int, item.split(','))) for item in pages]

def checkifinrules(pages):

def checkifrulevio(pages):
  for rule in rules:
    for element in pages:




def add():
  print("Bla")
  
for element in pages:
  if checkifrulevio(element):
    sum += add(element)
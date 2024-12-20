import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "input.txt")

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

# ------------------------------------------------------------------------------

pages
rules

def checkifrulevio(rule,pages):
  page_edited = []
  reversed_rule = []
  reversed_rule.append(rule[1])
  reversed_rule.append(rule[0])

  for index, x in enumerate(pages):
    if x == rule[0] or x == rule[1]:
      page_edited.append(x)
  if page_edited == reversed_rule:
    return False
  else:
    return True

def checkifrulesvio(pages, rules):
  for rule in rules:
    if checkifrulevio(rule, pages) == False:
      return False
  return True

sum = 0

for page in pages:
  if checkifrulesvio(page, rules):
    middle = int((len(page)+1)/2) - 1
    sum += page[middle]

print(sum)



  



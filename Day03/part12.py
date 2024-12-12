#Read input data
with open('input.txt', 'r') as file:
  data = file.read()

print(data)
print(len(data))


def calc(number1, number2):
  n1 = 0
  n2 = 0
  number1char = '0'
  number2char = '0'
  number1char = ''.join(number1)
  number2char = ''.join(number2)
  n1 = int(number1char)
  n2 = int(number2char)
  print(n1)
  print(n2)
  return n1 * n2

sum = 0
state = "m"
state2 = 'd'
mul_counter = 0
number1 = []
number2 = []
do = True

for i in data:
  print(i)
  if do:
    #m
    if state == "m":
      if i == 'm':
        state = "u"
      else:
        state = "m"

    #u
    elif state == "u":
      if i == 'u':
        state = "l"
      else:
        state = "m"

    #l
    elif state == "l":
      if i == 'l':
        state = "("
      else:
        state = "m"

    #(
    elif state == "(":
      if i == '(':
        state = "d11"
      else:
        state = "m"

    #d11
    elif state == "d11":
      if i.isdigit():
        state = "d12"
        number1.clear()
        number1.append(i)
      else:
        state = "m"
      
    #d12
    elif state == "d12":
      if i.isdigit():
        state = "d13"
        number1.append(i)
      elif i == ',':
        state = "d21"
      else:
        state = "m"

    #d13
    elif state == "d13":
      if i.isdigit():
        state = ","
        number1.append(i)
      elif i == ',':
        state = "d21"
      else:
        state = "m"

    #,
    elif state == ",":
      if i == ',':
        state = "d21"
      else:
        state = "m"

    #d21
    elif state == "d21":
      if i.isdigit():
        state = "d22"
        number2.clear()
        number2.append(i)
      else:
        state = "m"

    #d22
    elif state == "d22":
      if i.isdigit():
        state = "d23"
        number2.append(i)
      elif i == ')':
        state = "m"
        print("FOUND CORRECT MUL")
        sum += calc(number1, number2)
      else:
        state = "m"

    #d23
    elif state == "d23":
      if i.isdigit():
        state = ")"
        number2.append(i)
      elif i == ')':
        state = "m"
        print("FOUND CORRECT MUL")
        sum += calc(number1, number2)
      else:
        state = "m"

    #)
    elif state == ")":
      if i == ')':
        state = "m"
        print("FOUND CORRECT MUL")
        sum += calc(number1, number2)
      else:
        state = "m"

    #search for don't()

    #d
    if state2 == "d":
      if i == 'd':
        state2 = "o"
      else:
        state2 = "d"
    elif state2 == "o":
      if i == 'o':
        state2 = "n"
      else:
        state2 = "d"
    elif state2 == "n":
      if i == 'n':
        state2 = "'"
      else:
        state2 = "d"
    elif state2 == "'":
      if i == "'":
        state2 = "t"
      else:
        state2 = "d"
    elif state2 == "t":
      if i == "t":
        state2 = "d"
        do = False
      else:
        state2 = "d"
  else:
    if state2 == "d":
      if i == "d":
        state2 = "o"
      else:
        state2 = "d"
    elif state2 == "o":
      if i == "o":
        state2 = "("
      else:
        state2 = "d"
    elif state2 == "(":
      if i == "(":
        state2 = ")"
      else:
        state2 = "d"
    elif state2 == ")":
      if i == ")":
        do = True
        state2 = "d"
      else:
        state2 = "d"

print(sum)
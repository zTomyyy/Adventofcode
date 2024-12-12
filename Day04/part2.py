import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "input.txt")

# Datei einlesen
with open(file_path, "r") as file:
    lines = file.readlines()

# Jede Zeile in eine Liste von Zeichen umwandeln
matrix = [list(line.strip()) for line in lines]

def get_a_matrix(x, y, matrix):
  amatrix = [[0] * 3 for _ in range(3)]

   
def check_if_xmas(amatrix)
   

xmas = 0

for y, element in enumerate(matrix):
  for x in element:
    if x == "A":
      if check_if_xmas(get_a_matrix(x,y,matrix)):
         xmas += 1

print(f"X-Mas found: {xmas}")
            
        


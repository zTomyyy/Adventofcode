import os
import copy

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "input.txt")

# Datei einlesen
with open(file_path, "r") as file:
  lines = file.readlines()

# Jede Zeile in eine Liste von Zeichen umwandeln
matrix = [list(line.strip()) for line in lines]

def get_a_matrix(y, x, matrix):
  amatrix = [[0] * 3 for _ in range(3)]
  for yin in range(3):
    for xin in range(3):
      amatrix[yin][xin] = matrix[yin+y-1][xin+x-1]
  amatrix[0][1] = '0'
  amatrix[1][0] = '0'
  amatrix[2][1] = '0'
  amatrix[1][2] = '0'
  return amatrix

def check_if_xmas(matrix):
  check_matrix = [['M', '0', 'M'],
                  ['0', 'A', '0'],
                  ['S', '0', 'S']]
  for i in range(4):
    if check_matrix == matrix:
      return True
    check_matrix = rotatematrix(check_matrix)
  

def rotatematrix(matrix):
  rotated_matrix = [[0] * 3 for _ in range(3)]
  rotated_matrix = copy.deepcopy(matrix)
  rotated_matrix[0][2] = matrix[0][0]  # oben links → oben rechts
  rotated_matrix[2][2] = matrix[0][2]  # oben rechts → unten rechts
  rotated_matrix[2][0] = matrix[2][2]  # unten rechts → unten links
  rotated_matrix[0][0] = matrix[2][0]  # unten links → oben links

  return rotated_matrix

xmas = 0

for y in range(len(matrix)-2):
  for x in range(len(matrix[0])-2):
    if matrix[y+1][x+1] == "A":
      if check_if_xmas(get_a_matrix(y+1,x+1,matrix)):
        xmas += 1

print(f"X-Mas found: {xmas}")

           
        


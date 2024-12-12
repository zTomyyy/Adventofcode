# Datei einlesen
with open("input.txt", "r") as file:
    lines = file.readlines()

# Jede Zeile in eine Liste von Zeichen umwandeln
matrix = [list(line.strip()) for line in lines]

# Vertikal in beide Richtungen testen
def checkvertical(matrix):
  compare = [['S', 'A', 'M', 'X'], ['X', 'M', 'A', 'S']]
  comparearray = ['0', '0', '0', '0']
  xmas = 0
  for i in range(0, 2):
    for row in matrix:
      for x in range(0, len(row)-3):
        for y in range(0, 4):
          comparearray[y] = row[x+y]
        if comparearray == compare[i]:
          xmas += 1
  return xmas

# Array um 90°
def rotatematrix(matrix):
  rotated_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]  
  for y, ye in enumerate(matrix):
    for x, xe in enumerate(ye):
      rotated_matrix[x][y] = xe
  return rotated_matrix

# Diagonal zu Horizontal
def get_diagonals(grid: list, rows: int, cols: int) -> list:
  '''
  Function to convert the diagonals into lists.

  Parameters
  ----------
  grid : list
      The 2D matrix
  
  rows : int
      Number of rows in grid

  cols : int
      Number of coloumns in grid

  Returns
  -------
  list
      List containing both diagonals as strings
  '''
  diagonals = []
  # Top-left to bottom-right diagonals
  for d in range(rows + cols - 1):
      diag1 = []
      diag2 = []
      for row in range(max(0, d - cols + 1), min(rows, d + 1)):
          col = d - row
          diag1.append(grid[row][col])
          diag2.append(grid[row][cols - col - 1])
      diagonals.append(''.join(diag1))
      diagonals.append(''.join(diag2))
  return diagonals

xmas = 0
xmas += checkvertical(matrix)
matrix = rotatematrix(matrix)
xmas += checkvertical(matrix)
xmas += checkvertical(get_diagonals(matrix, len(matrix), len(matrix[0])))
print(get_diagonals(matrix, len(matrix), len(matrix[0])))
print(xmas)
















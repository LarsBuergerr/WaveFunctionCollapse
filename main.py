from tkinter.tix import COLUMN
from State1 import state1
from State3 import state3
from UniObj import uniObj

def main():
  ROWS     = 4
  COLUMNS = 4

  collapsed = state1()
  surrounding = state3()

  surrounding.calculate(collapsed.valid)

  matrix = [['1'] * COLUMNS] * ROWS

  for i in range(ROWS):
    for j in range(COLUMNS):
      matrix[i][j] = uniObj()
      matrix[i][j].printObj(i, j)
      #print(matrix[i][j], end=' ')
    print()


  for x in collapsed.valid:
    if x[0] == 'state1':
      print(x[1])


if __name__ == "__main__":
  main()
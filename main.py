from Obj1 import obj1
from Obj3 import obj3

def main():
  collapsed = obj1()
  surrounding = obj3()

  surrounding.calculate(collapsed.valid)

  print(surrounding.valid)



if __name__ == "__main__":
  main()
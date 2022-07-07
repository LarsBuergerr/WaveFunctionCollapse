class obj2:

  name = 'obj2'
  valid = []

  def __init__(self):
    self.valid.extend(['obj1', 'obj2', 'obj3', 'obj4'])

  def calculate(self, list):
    tmp = set(self.valid) & set(list)
    self.valid = tmp

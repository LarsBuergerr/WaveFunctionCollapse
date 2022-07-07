class obj1:

  name = 'obj1'
  valid = []

  def __init__(self):
    self.valid.extend(['obj1', 'obj2'])

  def calculate(self, list):
    tmp = set(self.valid) & set(list)
    self.valid = tmp

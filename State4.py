class state4:

  name = 'state4'
  valid = []

  def __init__(self):
    self.valid.extend([('state1', 20), ('state2', 50),('state3', 30), ('state4', 0)])

  def calculate(self, list):
    tmp = set(self.valid) & set(list)
    self.valid = tmp
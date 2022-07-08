class uniObj:

  valid = []
  collapsed = False
  collapsedState = ' '


  def __init__(self):
    self.valid.extend(['state1', 'state2', 'state3', 'state4'])

  def printObj(self, x, y):
    print('Obj[%s][%s]' % (x, y), end=' ')

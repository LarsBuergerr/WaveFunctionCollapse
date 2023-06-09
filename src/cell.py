
class Cell():
    
    def __init__(self, x, y, value, allowed_states):
        
        self._x = x
        self._y = y
        self._value = value
        self._allowed_values = allowed_states
        self._collapsed = False
    
    def __str__(self):
        return f"Cell({self.x}, {self.y}, {self.value}, {self.allowed_values})"
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def value(self):
        return self._value
    
    @property
    def allowed_values(self):
        return self._allowed_values
    
    @property
    def collapsed(self):
        return self._collapsed
    
    @value.setter
    def value(self, value):
        self._value = value
        
    @allowed_values.setter
    def allowed_values(self, allowed_values):
        self._allowed_values = allowed_values
    
    
    @collapsed.setter
    def collapsed(self, collapsed):
        self._collapsed = collapsed
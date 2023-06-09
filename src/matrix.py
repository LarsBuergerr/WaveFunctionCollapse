from cell import Cell

class Matrix():
    
    def __init__(self, rows, cols, states):
        
        self.rows = rows
        self.cols = cols
        self.states = states
        self.m = self.create_matrix()
        
    
    def create_matrix(self):
        """Create a matrix of size rows x cols"""
        matrix = []
        for row in range(self.rows):
            matrix.append([])
            for col in range(self.cols):
                matrix[row].append(Cell(row, col, None, self.states))
        return matrix
    
    def __str__(self):
        """prints the matrix with the value of the cells"""
        
        string = ""
        for row in self.m:
            for cell in row:
                if cell.value == None:
                    string += " "
                else:
                    string += str(cell.value)
            string += "\n"
        return string
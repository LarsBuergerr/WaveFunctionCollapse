import random

from cell import Cell
from matrix import Matrix
from rules import *

class WFC():
    
    def __init__(self, rows, cols, states):
        
        self.rows = rows
        self.cols = cols
        self.states = states
        self.matrix = Matrix(rows, cols, states)     

    def find_lowest_entropy(self):
        """Find the cell with the lowest entropy (the one with the least amount of states)"""

        lowest_entropies = []
        lowest_score = len(self.states) + 1

        for row in self.matrix.m:
            for cell in row:
                if not cell.collapsed:
                    score = len(cell.allowed_values)
                    if score < lowest_score:
                        lowest_entropies = [cell]
                        lowest_score = score
                    elif score == lowest_score:
                        lowest_entropies.append(cell)

        # return random cell from lowest entropies
        return random.choice(lowest_entropies)


    def collapse(self, cell):
        """Collapse the cell to a random state"""
        cell.value = random.choice(list(cell.allowed_values))
        cell.allowed_values = {cell.value}
        cell.collapsed = True


    def get_neighbours(self, cell):
        """Get the neighbours of the cell"""
        neighbours = []
        if cell.x > 0:
            neighbours.append((self.matrix.m[cell.x - 1][cell.y], valid_top)) # top neighbour
        if cell.x < self.rows - 1:
            neighbours.append((self.matrix.m[cell.x + 1][cell.y], valid_bot)) # bottom neighbour
        if cell.y > 0:
            neighbours.append((self.matrix.m[cell.x][cell.y - 1], valid_left)) # left neighbour
        if cell.y < self.cols - 1:
            neighbours.append((self.matrix.m[cell.x][cell.y + 1], valid_right)) # right neighbour
        return neighbours
        
        
    def update_neighbours(self, cell):
        """Update the allowed values of the neighbours of the cell"""
        for entry in self.get_neighbours(cell):
            neighbour = entry[0]
            direction = entry[1]
            
            if neighbour.collapsed:
                continue
            # remove all values from the neighbour that are not allowed
            neighbour.allowed_values = neighbour.allowed_values.intersection(direction[cell.value])
            

if __name__ == '__main__':
    wfc = WFC(100, 100, {'║', '╣', '╗', '╔', '╝', '╚', '╩', '╦', '╠', '═', '╬'})
    
    entry_count = wfc.rows * wfc.cols
    
    while entry_count > 0:
        cell = wfc.find_lowest_entropy()
        wfc.collapse(cell)
        wfc.update_neighbours(cell)
        entry_count -= 1

        print(wfc.matrix)
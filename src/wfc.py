import random
import json
import copy

from cell import Cell
from matrix import Matrix
from state import State

class WFC():
    
    def __init__(self, rows, cols):
        
        self.rows = rows
        self.cols = cols
        self.rules = self.define_ruleset()
        self.matrix = Matrix(rows, cols, self.rules)
        self.finished = False


    def define_ruleset(self):
        f = open('rules.json', encoding='utf-8', mode='r')
        data = json.load(f)
        
        # define ruleset
        ruleset = []

        for entry in data:
            entry_data = data[entry]
            
            for i in range(4):
                state = State(str(entry) + "_" + str(i), "../images/circuit/" + str(entry) + ".png", i, entry_data)

                # check if state.side_rules is already in ruleset
                # if not, add it
                if not any(state.side_rules == rule.side_rules for rule in ruleset):
                    ruleset.append(state)

        # remove rules that have the exact same side_rules


        print(len(ruleset))  
        for state in ruleset: print(state)
        return ruleset


    def find_lowest_entropy(self):
        """Find the cell with the lowest entropy (the one with the least amount of states)"""

        lowest_entropies = []
        lowest_score = len(self.rules) + 1

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
        if len(cell.allowed_values) == 0:

            # print all neighbours and their collapsed state
            for entry in self.get_neighbours(cell):
                neighbour = entry[0]
                direction = entry[1]

            cell.value = State("error", "../images/circuit/error_tile.png", 0, ["AAA", "AAA", "AAA", "AAA"])
        else:
            cell.value = random.choice(list(cell.allowed_values))
        cell.allowed_values = {cell.value}
        cell.collapsed = True

    # @TODO remove int numbs for directions
    def get_neighbours(self, cell):
        """Get the neighbours of the cell"""
        neighbours = []
        if cell.x > 0:
            neighbours.append((self.matrix.m[cell.x - 1][cell.y], 0)) # top neighbour
        if cell.x < self.rows - 1:
            neighbours.append((self.matrix.m[cell.x + 1][cell.y], 2)) # bottom neighbour
        if cell.y > 0:
            neighbours.append((self.matrix.m[cell.x][cell.y - 1], 3)) # left neighbour
        if cell.y < self.cols - 1:
            neighbours.append((self.matrix.m[cell.x][cell.y + 1], 1)) # right neighbour
        return neighbours
        
        
    def update_neighbours(self, cell):
        """Update the allowed values of the neighbours of the cell"""
        for entry in self.get_neighbours(cell):
            neighbour = entry[0]
            direction = entry[1]
            
            if neighbour.collapsed:
                continue

            # remove all values from the neighbour that are not allowed
            allowed_values = []
            
            for state in neighbour.allowed_values:

                state_string = copy.copy(cell.value.side_rules[direction])
                reversed_string = state_string[::-1]

                if reversed_string == state.side_rules[(direction + 2) % 4]:
                    allowed_values.append(state)

            neighbour.allowed_values = allowed_values

    def run(self):
        """Run the wfc algorithm"""
        total_cells = self.rows * self.cols

        while total_cells - 1 >= 0:
            cell = self.find_lowest_entropy()
            self.collapse(cell)
            self.update_neighbours(cell)
            total_cells -= 1
        
        self.finished = True


if __name__ == "__main__":
    wfc = WFC(10, 10)
    wfc.run()
# Wave function collapse algorithm implementation
import os
import random
import time
import sys

valid_states = {
    's1': {'s2', 's4', 's5'},
    's2': {'s1', 's4', 's5'},
    's3': {'s1', 's2', 's4'},
    's4': {'s1', 's2', 's5'},
    's5': {'s2', 's4', 's5'},
}


def calc_neighbours(o):
    ox = o.x
    oy = o.y

    neighbour_cords = [[ox - 1, oy],
                       [ox, oy - 1],
                       [ox + 1, oy],
                       [ox, oy + 1]]

    for cords in neighbour_cords:
        if (0 <= cords[0] <= ROWS - 1) and (0 <= cords[1] <= COLUMNS - 1) \
                and len(matrix[cords[0]][cords[1]].states) > 1:
            matrix[cords[0]][cords[1]].calc_new_states(o.collapsed_state)

def collapse_lowest():
    selected = None
    l = []
    lowest = TOTAL_STATES

    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            if matrix[i][j] == 1 and not matrix[i][j].collapsed:
                lowest = 1
                matrix[i][j].collapsed = True
                matrix[i][j].collapsed_state = matrix[i][j].states.pop()
                l.append(matrix[i][j])

            elif len(matrix[i][j].states) < lowest and len(matrix[i][j].states) != 1:
                lowest = len(matrix[i][j].states)

    if lowest == 1:
        return l
    else:
        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if len(matrix[i][j].states) == lowest:
                    l.append(matrix[i][j])

        if len(l) is not None and len(l) > 0:
            rand = random.randint(0, len(l) - 1)
        else:
            return

        selected = l[rand]
        selected.collapsed = True
        ran = random.choice(list(selected.states))
        selected.states = {ran}
        selected.collapsed_state = ran
        return [selected]


def print_matrix():
    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            print(len(matrix[i][j].states), end=' ') if len(matrix[i][j].states) > 1 else print('O', end=' ')
        print()


class Obj:
    collapsed = False
    collapsed_state = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    states = {'s1', 's2', 's3', 's4', 's5'}

    def calc_new_states(self, state):
        self.states = self.states & valid_states.get(state)


if __name__ == '__main__':
    ROWS = 40
    COLUMNS = 40
    MATRIX_ENTRIES = ROWS * COLUMNS
    TOTAL_STATES = 5
    total_collapsed = 1

    matrix = [[0] * COLUMNS for _ in range(ROWS)]

    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            matrix[i][j] = Obj(i, j)

    print_matrix()
    print()

    randx = random.randint(0, ROWS - 1)
    randy = random.randint(0, COLUMNS - 1)

    matrix[randx][randy].states = {'s1'}
    matrix[randx][randy].collapsed = True
    matrix[randx][randy].collapsed_state = 's3'

    calc_neighbours(matrix[randx][randy])

    print_matrix()

    while total_collapsed < MATRIX_ENTRIES:
        c = collapse_lowest()

        if not c: break

        count = len(c)
        total_collapsed += count

        for entry in c:
            calc_neighbours(entry)

        print_matrix()
        print()
        os.system('clear')

    print_matrix()
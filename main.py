# Wave function collapse algorithm implementation
import os
import random
import time
import sys

valid_top = {
    '║': {'║', '╣', '╝', '╚', '╩', '╠'},
    '╣': {'║', '╣', '╝', '╚', '╩', '╠'},
    '╗': {'║', '╣', '╝', '╚', '╩', '╠'},
    '╔': {'║', '╣', '╝', '╚', '╩', '╠'},
    '╝': {'╗', '╔', '═', '╦'},
    '╚': {'╗', '╔', '═', '╦'},
    '╩': {'╗', '╔', '═', '╦'},
    '╦': {'║', '╣', '╝', '╚', '╩', '╠'},
    '╠': {'║', '╣', '╝', '╚', '╩', '╠'},
    '═': {'╗', '╔', '═', '╦'},
    #'╬': {'║', '╣', '╝', '╚', '╩', '╠'},

}

valid_bot = {
    '║': {'║', '╣', '╠', '╦', '╔', '╗'},
    '╣': {'║', '╣', '╠', '╦', '╔', '╗'},
    '╗': {'╝', '╚', '╩', '═'},
    '╔': {'╝', '╚', '╩', '═'},
    '╝': {'║', '╣', '╠', '╦', '╔', '╗'},
    '╚': {'║', '╣', '╠', '╦', '╔', '╗'},
    '╩': {'║', '╣', '╠', '╦', '╔', '╗'},
    '╦': {'╝', '╚', '╩', '═'},
    '╠': {'║', '╣', '╠', '╦', '╔', '╗'},
    '═': {'╝', '╚', '╩', '═'},
    #'╬':{'║', '╣', '╠', '╦', '╔', '╗'},
}

valid_right = {
    '║': {'╝', '╣', '║', '╗'},
    '╣': {'╚', '╩', '╦', '╔', '╠', '═'},
    '╗': {'╚', '╩', '╦', '╔', '╠', '═'},
    '╔': {'╝', '╣', '║', '╗'},
    '╝': {'╚', '╩', '╦', '╔', '╠', '═'},
    '╚': {'╝', '╣', '║', '╗'},
    '╩': {'╚', '╩', '╦', '╔', '╠', '═'},
    '╦': {'╚', '╩', '╦', '╔', '╠', '═'},
    '╠': {'╝', '╣', '║', '╗'},
    '═': {'╚', '╩', '╦', '╔', '╠', '═'},
    #'╬': {'╚', '╩', '╦', '╔', '╠', '═'},
}

valid_left = {
    '║': {'╚', '║', '╠', '╔'},
    '╣': {'╚', '║', '╠', '╔'},
    '╗': {'╚', '║', '╠', '╔'},
    '╔': {'╝', '╩', '╦', '═', '╗', '╣'},
    '╝': {'╚', '║', '╠', '╔'},
    '╚': {'╝', '╩', '╦', '═', '╗', '╣'},
    '╩': {'╝', '╩', '╦', '═', '╗', '╣'},
    '╦': {'╝', '╩', '╦', '═', '╗', '╣'},
    '╠': {'╝', '╩', '╦', '═', '╗', '╣'},
    '═': {'╝', '╩', '╦', '═', '╗', '╣'},
    #'╬': {'╝', '╩', '╦', '═', '╗', '╣'},
}


def calc_neighbours(o):
    c = 0
    ox = o.x
    oy = o.y

    neighbour_cords = [[ox - 1, oy],
                       [ox, oy - 1],
                       [ox + 1, oy],
                       [ox, oy + 1]]

    for cords in neighbour_cords:
        if (0 <= cords[0] <= ROWS - 1) and (0 <= cords[1] <= COLUMNS - 1) \
                and len(matrix[cords[0]][cords[1]].states) > 1:

                matrix[cords[0]][cords[1]].calc_new_states(o.collapsed_state, c)
        c += 1



def collapse_lowest():
    selected = None
    l = []
    lowest = TOTAL_STATES

    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            if len(matrix[i][j].states) == 1 and not matrix[i][j].collapsed:
                lowest = 1
                matrix[i][j].collapsed = True
                matrix[i][j].collapsed_state = matrix[i][j].states.pop()
                l.append(matrix[i][j])

            elif len(matrix[i][j].states) < lowest and len(matrix[i][j].states) > 1:
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
        selected.collapsed_state = ran
        selected.states = {ran}
        return [selected]


def print_matrix():
    for i in range(0, ROWS):
        for j in range(0, COLUMNS):

            if len(matrix[i][j].states) > 1:
                print(len(matrix[i][j].states), end='')
            else:
                print(matrix[i][j].collapsed_state, end='')
        print()


class Obj:
    collapsed = False
    collapsed_state = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    states = {'║', '╣', '╗', '╝', '╚', '╔', '╩', '╦', '╠', '═'}

    def calc_new_states(self, state, zk):
        if zk == 0:
            self.states = self.states & valid_bot.get(state)

        elif zk == 1:
            self.states = self.states & valid_right.get(state)

        elif zk == 2:
            self.states = self.states & valid_top.get(state)

        elif zk == 3:
            self.states = self.states & valid_left.get(state)

if __name__ == '__main__':
    ROWS = 50
    COLUMNS = 100
    MATRIX_ENTRIES = ROWS * COLUMNS
    TOTAL_STATES = 11
    total_collapsed = 1

    matrix = [[0] * COLUMNS for _ in range(ROWS)]

    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            matrix[i][j] = Obj(i, j)

    print_matrix()
    print()

    randx = random.randint(0, ROWS - 1)
    randy = random.randint(0, COLUMNS - 1)

    matrix[randx][randy].states = {'╠'}
    matrix[randx][randy].collapsed = True
    matrix[randx][randy].collapsed_state = '╠'

    calc_neighbours(matrix[randx][randy])

    print_matrix()

    while total_collapsed < MATRIX_ENTRIES:
        c = collapse_lowest()

        if not c: break

        count = len(c)
        total_collapsed += count

        for entry in c:
            calc_neighbours(entry)

        #print_matrix()
        #os.system('cls')

    print_matrix()

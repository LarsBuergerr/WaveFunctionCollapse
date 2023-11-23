import pygame
import random
import time
import sys

from wfc import WFC

class WFCSimulation():
    def __init__(self, rows, cols, cell_size):
        self.wfc = WFC(rows, cols)
        self.matrix_size = rows
        self.cell_size = cell_size
        self.window_size = rows * cell_size
        pygame.init()
        self.window = pygame.display.set_mode((self.window_size, self.window_size))

    def run(self):
        running = True
        current_cell = 0

        while current_cell < self.matrix_size * self.matrix_size:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

            self.window.fill((0, 0, 0))

            cell = self.wfc.find_lowest_entropy()
            self.wfc.collapse(cell)
            self.wfc.update_neighbours(cell)

            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    if current_cell >= i * self.matrix_size + j:
                        x = j * self.cell_size
                        y = i * self.cell_size

                        if self.wfc.matrix.m[i][j].collapsed:
                            cell_image = pygame.transform.scale(self.wfc.matrix.m[i][j].value.image, (self.cell_size, self.cell_size))
                            self.window.blit(cell_image, (x, y))
                        else:
                            pygame.draw.rect(self.window, (0, 0, 0), (x, y, self.cell_size, self.cell_size))

            pygame.display.flip()

            time.sleep(0.01)
            current_cell += 1

        # Keep the window open until the user closes it
        waiting_for_exit = True
        while waiting_for_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_exit = False
                elif event.type == pygame.KEYDOWN:
                    waiting_for_exit = False

        pygame.quit()

# Usage example
rows = 20
cols = 20
cell_size = 50

display = WFCSimulation(rows, cols, cell_size)
display.run()
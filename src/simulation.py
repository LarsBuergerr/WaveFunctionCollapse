import pygame
import random
import time

from wfc import WFC

class WFCSimulation():
    def __init__(self, rows, cols, cell_size):
        self.wfc = WFC(rows, cols)
        self.matrix_size = rows
        self.cell_size = cell_size
        self.window_size = rows * cell_size
        # Initialize pygame
        pygame.init()

        # Create the window
        self.window = pygame.display.set_mode((self.window_size, self.window_size))

    def run(self):
        # Main game loop
        running = True
        current_cell = 0

        while current_cell < self.matrix_size * self.matrix_size and running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the window
            self.window.fill((0, 0, 0))

            # run one step of the wfc algorithm
            cell = self.wfc.find_lowest_entropy()
            self.wfc.collapse(cell)
            self.wfc.update_neighbours(cell)

            # Draw the matrix

            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    if current_cell >= i * self.matrix_size + j:
                        # Calculate the position of the current cell
                        x = j * self.cell_size
                        y = i * self.cell_size

                        if self.wfc.matrix.m[i][j].collapsed:
                            cell_image = pygame.transform.scale(self.wfc.matrix.m[i][j].value.image, (self.cell_size, self.cell_size))
                            self.window.blit(cell_image, (x, y))
                        else:
                            pygame.draw.rect(self.window, (0, 0, 0), (x, y, self.cell_size, self.cell_size))


            # Update the display
            pygame.display.flip()

            # Sleep for 0.1 seconds
            time.sleep(0.01)

            # Increment the current cell counter
            current_cell += 1

        time.sleep(10000)
        # Quit the game
        # pygame.quit()

# Usage example
rows = 20
cols = 20
cell_size = 50

display = WFCSimulation(rows, cols, cell_size)
display.run()
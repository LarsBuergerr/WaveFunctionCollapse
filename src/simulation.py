import pygame
import random

from wfc import WFC

class MatrixDisplay:
    def __init__(self, rows, cols, cell_size, image_paths):
        self.wfc = WFC(rows, cols, image_paths)
        self.matrix_size = rows
        self.cell_size = cell_size
        self.window_size = rows * cols * cell_size

        # Initialize pygame
        pygame.init()

        # Create the window
        self.window = pygame.display.set_mode((self.window_size, self.window_size))

        # Load images
        self.images = []
        for path in image_paths:
            image = pygame.image.load(path)
            # Scale the images to fit the cell size
            image = pygame.transform.scale(image, (self.cell_size, self.cell_size))
            self.images.append(image)

        # Create the matrix with random image indices
        self.matrix = [[random.randint(0, len(self.images) - 1) for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]

    def run(self):
        # Main game loop
        running = True
        while running:
            print("here")
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the window
            self.window.fill((0, 0, 0))

            cell = self.wfc.find_lowest_entropy()
            self.wfc.collapse(cell)
            self.wfc.update_neighbours(cell)
            
            # Draw the matrix
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    # Calculate the position of the current cell
                    x = j * self.cell_size
                    y = i * self.cell_size

                    # Get the corresponding image
                    image = cell.value.image

                    # Draw the image onto the cell
                    self.window.blit(image, (x, y))

            # Update the display
            pygame.display.flip()

        # Quit the game
        pygame.quit()

# Usage example
rows = 10
cols = 10
cell_size = 50
image_paths = ['../images/circuit/0.png', '../images/circuit/1.png', '../images/circuit/2.png']  # Paths to the images

display = MatrixDisplay(rows, cols, cell_size,  image_paths)
display.run()
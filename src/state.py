import pygame
from collections import deque

class State():
    
    def __init__(self, name, image_path, rotate_angle, side_rules):
        self.name = name
        self.image_path = image_path
        self.rotate_angle = rotate_angle
        self.side_rules = self.rotate_sides(side_rules)
        self.image = self.rotate_image()
        
        
    def rotate_image(self):
        # return the image rotated to the right with the given angle
        image = pygame.image.load(self.image_path)
        image = pygame.transform.rotate(image, -(self.rotate_angle * 90))
        return image
    
    def rotate_sides(self, side_rules):
        # return the sides rotated to the right with the given angle
        sides = deque(side_rules)
        sides.rotate(self.rotate_angle)
        return list(sides)
    
    
    def __str__(self):
        return f"State({self.name}, {self.image_path}, {self.rotate_angle}, {self.side_rules})"
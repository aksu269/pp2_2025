import pygame
from game_object import GameObject 
from game_object import Point 

class Wall(GameObject):
    def __init__(self, tile_width):
        super().__init__([],(88, 57, 39), tile_width)
        self.level = 0
        self.load_level()

    def load_level(self):
        self.points = []  
        with open(f"levels/level{self.level}.txt", "r") as f:
            for row, line in enumerate(f): 
                for col, c in enumerate(line.strip()): 
                    if c == '#':
                        self.points.append(Point(col * self.tile_width, row * self.tile_width))



    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 2
        self.load_level()
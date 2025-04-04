import pygame
from game_object import GameObject 
from game_object import Point 

class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20)],(0,100,0), tile_width)
        self.DX = 1
        self.DY = 0

    def move(self):

        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width


    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))

    def process_input(self,  events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if self.DY != 1:
                    self.DX = 0
                    self.DY = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.DY != -1:
                    self.DX = 0
                    self.DY = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if self.DX != -1:
                    self.DX = 1
                    self.DY = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if self.DX != 1:
                    self.DX = -1
                    self.DY = 0
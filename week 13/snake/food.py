import pygame
import random, time
from wall import Wall
from game_object import GameObject 
from game_object import Point 

class Food(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(random.randint(0, 19)*tile_width, random.randint(0, 14)*tile_width)],(255,0,0), tile_width)
        self.type = 'special'
        self.weight = 3
        self.spawn_time = time.time()  

    def respawn(self, wall, worm):
        while True:
            test = Point(random.randint(0, 19)*self.tile_width, random.randint(0, 14)*self.tile_width)
            valid_position = True
            for wall_point in wall.points:
                if test.X == wall_point.X and test.Y == wall_point.Y:
                    valid_position = False
                    break

            for worm_point in worm.points:
                if test.X == worm_point.X and test.Y == worm_point.Y:
                    valid_position = False
                    break
            if valid_position:
                self.points[0] = test  
                if random.choice([True, False]):
                    self.type = "special"
                    self.weight = 3
                    self.color = (255, 0, 0)  
                else:
                    self.type = "normal"
                    self.weight = 1
                    self.color = (255, 255, 0)    
                self.spawn_time = time.time()  
                break 
    def update(self, wall, worm):
        if self.type == "special" and time.time() - self.spawn_time > 5:
            self.respawn(wall, worm)
    
                
    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
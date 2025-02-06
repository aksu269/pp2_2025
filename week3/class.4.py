class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates:", self.x, self.y)
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, sec_point):
        return (self.x - sec_point.x)**2 + (self.y - sec_point.y)**2
point1 = point(1, 2)
point2 = point(4, 4)
point2.move(3, 2)
distance = point1.dist(point2)
point2.show()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def move(self, x, y):
        self.x += x
        self.y += y
        
    def length(self, otherPoint):
        return round(((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2)**(1 / 2), 2)
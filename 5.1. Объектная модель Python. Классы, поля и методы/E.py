class Rectangle:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.a = abs(self.B[0] - self.A[0])
        self.b = abs(self.B[1] - self.A[1])

    def perimeter(self):
        return abs(round((self.a + self.b) * 2, 2))

    def area(self):
        return abs(round(self.a * self.b, 2))
    
#--------------
class Rectangle:
    def __init__(self, *coords):
        self.coords = coords
        self.width = abs(self.coords[0][0] - self.coords[1][0])
        self.height = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)
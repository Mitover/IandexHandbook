class Rectangle:
    def __init__(self, dot1, dot2) -> None:
        self.left_down_point = [min(dot1[0], dot2[0]), min(dot1[1], dot2[1])]
        self.up_right_point = [max(dot1[0], dot2[0]), max(dot1[1], dot2[1])]
    
    def perimeter(self):
        return round((self.up_right_point[0] - self.left_down_point[0]) * 2 +
                     (self.up_right_point[1] - self.left_down_point[1]) * 2, 2)

    def area(self):
        return round((self.up_right_point[0] - self.left_down_point[0]) *
                     (self.up_right_point[1] - self.left_down_point[1]), 2)

    def get_pos(self):
        return round(self.left_down_point[0], 2), round(self.up_right_point[1], 2)

    def get_size(self):
        return (round(self.up_right_point[0] - self.left_down_point[0], 2), 
                round(self.up_right_point[1] - self.left_down_point[1], 2))

    def move(self, dx, dy):
        self.left_down_point[0] += dx
        self.left_down_point[1] += dy
        self.up_right_point[0] += dx
        self.up_right_point[1] += dy

    def resize(self, width, height):
        self.up_right_point[0] = self.left_down_point[0] + width
        self.left_down_point[1] = self.up_right_point[1] - height
###
class Point:
    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def round(self):
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)
        return self


class Rectangle:
    def __init__(self, dot1, dot2) -> None:
        self.point = Point(min(dot1[0], dot2[0]), max(dot1[1], dot2[1]))  
        self.width = round(max(dot1[0], dot2[0]) - self.point.x, 2)
        self.height = round(self.point.y - min(dot1[1], dot2[1]), 2)

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)

    def area(self):
        return round(self.width * self.height, 2)
    
    def get_pos(self):
        return self.point.x, self.point.y

    def get_size(self):
        return self.width, self.height

    def move(self, dx, dy):
        self.point.x += dx
        self.point.y += dy
        self.point.round()

    def resize(self, width, height):
        self.width = round(width, 2)
        self.height = round(height, 2)


# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())


# rect = Rectangle((7.52, -4.3), (3.2, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.resize(23.5, 11.3)
# print(rect.get_pos(), rect.get_size())
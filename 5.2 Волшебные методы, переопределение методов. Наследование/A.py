class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        elif len(args) == 2:
            pass

# class PatchedPoint(Point):
#     def __init__(self, *args) -> None:
#         if len(args) == 0:
#             super().__init__(0, 0)
#         elif len(args) == 1:
#             super().__init__(*args[0])
#         elif len(args) == 2:
#             super().__init__(*args)

point = PatchedPoint()
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
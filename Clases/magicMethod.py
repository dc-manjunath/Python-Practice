class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return  Point(self.x + other.x,  self.y + other.y)


point = Point( 1 , 2)

other = Point(2, 4)

print(point + other)
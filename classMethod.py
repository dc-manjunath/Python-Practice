class Circle:
    pi = 3.14159

    @classmethod
    def from_radius(cls, radius):
        return cls(radius)
    
    def __init__(self, raduis):
        self._raduis = raduis

    def area(self):
        return self.pi * self._raduis**2
    

circle1 = Circle.from_radius(5)

print(circle1.area())
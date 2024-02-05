# Class : blueprint for creating new objects 
# Objects : instance of class 

# Constructor


class Point:
    # class Attribute - they are same all over the class instences
    # There class attribute can be accsed by both  object and class name. 
    
    default_colour = "yellow"
    # this __init___ is a special method that called when we create an object from the class
    # this method is also called as magic method or constructor
    # self is used to refer the current of object of the class 


    def __init__(self, x, y):
        # the method we call in the class should have atleast one parameter that will conventionally
        # called self
        self.x = x # these two x and y are point instance Attribute
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
         print(f"Point ({self.x}, {self.y})")


point = Point(1,3)
# If I update the vaule of class attribute  using one  object, it will  reflect throughout that class"s  instances 
point.default_colour = "red"
print(point)

# from abc import ABC, abstractmethod

# class InvalidOperationError(Exception):
#     pass

# #ABCs are not directly instantiable (you cannot create objects directly from them)
# #They must be subclassed to provide concrete implementations of the methods declared in the base class
# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStraem(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream")

# stream = MemoryStream()
# stream.open()


from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def  area(self):
        return 3.14159*self.radius**2
    
    def  perimeter(self):
        return 2*3.14159*self.radius
    
class Square(Shape):
    def  __init__(self, side_lenght):
        self.side_length=side_lenght

    def  area(self):
        return self.side_length**2
    
    def   perimeter(self):
        return  4*self.side_length
    
class triangle(Shape):
    def  __init__(self, base, lenght):
        self.base=base
        self.lenght=lenght

    def area(self):
        return  (self.base*self.lenght)/2
    
    def perimeter(self):
        return  self.base + self.lenght*2
    

triangle_area = triangle(4, 6).area()
print(triangle_area)

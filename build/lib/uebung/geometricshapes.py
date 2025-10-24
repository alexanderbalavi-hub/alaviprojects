# define some geometric shapes

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return 3.14 * (self.radius ** 2)
        
class Square:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side * self.side
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):    
        return self.width * self.height        
    

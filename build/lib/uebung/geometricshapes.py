# define some geometric shapes

class Circle:
    """
    A class used to represent a Circle.
    Attributes
    ----------
    radius : float
        The radius of the circle.
    Methods
    -------
    getArea():
        Calculates and returns the area of the circle.
    """

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
    
    # ...existing code...
    
class Parallelogram:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def getPerimeter(self):
        return 2 * (self.side_a + self.side_b)
    
    # Beispiel:
    # parallelogram = Parallelogram(5, 10)
    # print(parallelogram.getPerimeter())  # Ausgabe: 30    
    

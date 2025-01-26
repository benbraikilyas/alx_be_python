import math

class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2




from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    shapes = [
        Rectangle(1 ,34),
        Circle(2)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

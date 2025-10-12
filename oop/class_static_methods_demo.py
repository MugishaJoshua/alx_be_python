# polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Represents a rectangle shape."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle shape."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

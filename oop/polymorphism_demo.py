import math

# Base class
class Shape:
    def area(self):
        """Raises an error if the area method is not implemented in the derived class."""
        raise NotImplementedError("The area method must be overridden in a subclass")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of a rectangle."""
        return self.length * self.width

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of a circle using π * radius^2."""
        return math.pi * self.radius ** 2
import math

# Base class for shapes
class Shape:
    def area(self):
        """Method to calculate the area of the shape.
        Should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method")

# Derived class for rectangles
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate rectangle area."""
        return self.length * self.width

# Derived class for circles
class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate circle area."""
        return math.pi * (self.radius ** 2)

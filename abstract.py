from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):    # shape is an abstract method
    @abstractmethod
    def area(self):
        pass

    def display(self):    # disoplay is a concrete method
        print("This is a shape.")

# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Subclass 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
circle.display() 
print("Area of Circle:", circle.area())

rectangle = Rectangle(4, 6)
rectangle.display()  
print("Area of Rectangle:", rectangle.area())

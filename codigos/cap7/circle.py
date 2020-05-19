'''
How to program in Python - Chapter 7
Derived class inheriting from a base class.
'''

import math


class Point:
    """Class that represents geometric point"""

    def __init__(self, x_value=0, y_value=0):
        """Point constructor takes x and y coordinates"""
        self.x_coordinate = x_value
        self.y_coordinate = y_value


class Circle(Point):
    """Class that represents a circle"""

    def __init__(self, x_value=0, y_value=0, radius_value=0.0):
        """Circle constructor takes x and y coordinates of center point and radius"""
        Point.__init__(self, x_value, y_value)  # call base-class constructor
        self.radius = float(radius_value)

    def area(self):
        """Computes area of a Circle"""
        return math.pi * self.radius ** 2

def main():
    '''Main program'''
    # examine classes Point and Circle
    print("Point bases:", Point.__bases__)
    print("Circle bases:", Circle.__bases__)

    # demonstrate class relationships with built-in function issubclass
    print("\nCircle is a subclass of Point:", issubclass(Circle, Point))
    print("\nPoint is a subclass of Circle:", issubclass(Point, Circle))

    point = Point(30, 50)  # create Point object
    circle = Circle(120, 89, 3)  # create Circle object

    # demonstrate object relationship with built-in function isinstance
    print("\ncircle is a Point object:", isinstance(circle, Point))
    print("\npoint is a Circle object:", isinstance(point, Circle))

    # print Point and Circle objects
    print("\npoint members:\n\t", point.__dict__)
    print("\ncircle members:\n\t", circle.__dict__)

    print("\nArea of circle:", circle.area())

main()

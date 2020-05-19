'''
How to program in Python - Chapter 7
Definition and test function for class Cylinder.
'''

import math
from pointmodule import Point
from circlemodule import Circle


class Cylinder(Circle):
    """Class that represents a cylinder"""

    def __init__(self, x, y, radius, height):
        """Constructor for Cylinder takes x, y, height and radius"""

        Circle.__init__(self, x, y, radius)
        self.height = float(height)

    def area(self):
        """Calculates (surface) area of a Cylinder"""

        return 2 * Circle.area(self) + 2 * math.pi * self.radius * self.height

    def volume(self):
        """Calculates volume of a Cylinder"""
        return Circle.area(self) * self.height

    def __str__(self):
        """String representation of a Cylinder"""
        return "{}; Height = {:f}".format(Circle.__str__(self), self.height)

def main():
    '''Main program'''
    # create object of class Cylinder
    cylinder = Cylinder(12, 23, 2.5, 5.7)

    # print Cylinder attributes
    print("X coordinate is:", cylinder.x)
    print("Y coordinate is:", cylinder.y)
    print("Radius coordinate is:", cylinder.radius)
    print("Height coordinate is:", cylinder.height)

    # change Cylinder attributes
    cylinder.height = 10
    cylinder.radius = 4.25
    cylinder.x, cylinder.y = 2, 2

    print("\nThe new points, radius and height of cylinder are:", cylinder)
    print("\nThe area of cylinder is: {:.2f}".format(cylinder.area()))
    print("\nThe volume of cylinder is: {:.2f}".format(cylinder.volume()))

    # display the Cylinder as a Point
    print("\ncylinder printed as a Point is:", Point.__str__(cylinder))

    # display the Cylinder as a Circle
    print("\ncylinder printed as a Circle is:", Circle.__str__(cylinder))


if __name__ == "__main__":
    main()

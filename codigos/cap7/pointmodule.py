'''
How to program in Python - Chapter 7
Definition and test function for class Point.
'''

class Point:
    """Class that represents a geometric point"""

    def __init__(self, xValue=0, yValue=0):
        """Point constructor takes x and y coordinates"""

        self.x = xValue
        self.y = yValue

    def __str__(self):
        """String representation of a Point"""
        return "({:d}, {:d} )".format(self.x, self.y)

def main():
    '''Main program'''
    point = Point(72, 115)

    print("X coordinate is:", point.x)
    print("Y coordinate is:", point.y)

    point.x = 10
    point.y = 10

    print("The new location of point is:", point)


if __name__ == "__main__":
    main()

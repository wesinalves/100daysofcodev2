'''
How to program in Python - Chapter 7
Overriding base-class methods.
'''

class Employee:
    """Class to represent an employee"""

    def __init__(self, first, last):
        """Employee constructor takes first and last name"""
        self.first_name = first
        self.last_name = last

    def __str__(self):
        """String representation of an Employee"""

        return "{} {}".format(self.first_name, self.last_name)


class HourlyWorker(Employee):
    """Class to represent an employee paid by hour"""

    def __init__(self, first, last, init_hours, init_wage):
        """Constructor for HourlyWorker, takes first and last name,
        23 initial number of hours and initial wage"""

        Employee.__init__(self, first, last)
        self.hours = float(init_hours)
        self.wage = float(init_wage)

    def get_pay(self):
        """Calculates HourlyWorker's weekly pay"""

        return self.hours * self.wage

    def __str__(self):
        """String representation of HourlyWorker"""

        print("HourlyWorker.__str__ is executing")

        return "{} is an hourly worker with pay of ${:.2f}".format(Employee.__str__(self), \
            self.get_pay())

def main():
    '''Main program'''
    hourly = HourlyWorker("Bob", "Smith", 40.0, 10.00)

    # invoke __str__ method several ways
    print("Calling __str__ several ways...")
    print(hourly)
    print(hourly.__str__())
    print(HourlyWorker.__str__(hourly))

main()

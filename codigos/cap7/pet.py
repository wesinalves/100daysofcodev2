'''
How to program in Python - Chapter II
Creating a class hierarchy with an abstract base class.
'''

import math

class Pet:
    """Abstract base class for pet"""

    def __init__(self, name, age):
        '''Construtor for class pet'''
        if self.__class__ == Pet:
            raise NotImplementedError('Cannot create object of class Employee')
        self.name = name
        self.age = age
    def __str__(self):
        '''String representation of Pet'''
        return '{:s} {:d}'.format(self.name, self.age)
    def food(self):
        '''Abstract method to comput how much food it requires'''
        raise NotImplementedError('Cannot call abstract method')
    def _human_age(self, value):
        '''Utility method to compute human age'''
        return math.log(value) * 16 + 31
class Dog(Pet):
    '''Abstract class for Dog'''

    def __init__(self, name, age, weight):
        '''Constructor for class Dog'''
        if self.__class__ == Dog:
            raise NotImplementedError('Cannot create object of class Employee')
        Pet.__init__(self, name, age)
        self.weight = weight
        self.human_age = self._human_age(int(age))
    def food(self):
        '''Compute how much food it requires'''
        required = 0

        if 0 < self.weight < 3:
            required = self.weight * 7 / 100
        elif 3 < self.weight < 5:
            required = self.weight * 6 / 100
        elif 5 < self.weight < 10:
            required = self.weight * 5 / 100
        elif 10 < self.weight < 22:
            required = self.weight * 4 / 100
        else:
            required = self.weight * 3.5 / 100
        return '{} Kg'.format(required)
    def __str__(self):
        '''String representation of Dog'''
        return '{:>10s} {:s}'.format('Dog', Pet.__str__(self))
class Beagle(Dog):
    '''Concrete class,  inherits from Pet'''

    def __init__(self, *args, **kwargs):
        '''Beagle constructor, takes a list and a dict as argument'''
        Dog.__init__(self, kwargs['name'], kwargs['age'], kwargs['weight'])
        self.height = kwargs['height']
        self.width = kwargs['width']
        self.colors = args
    def __str__(self):
        '''String representation of Beagle'''
        return '{:10}: {:s}'.format(Dog.__str__(self), 'Beagle')
    def _human_age(self, value):
        '''Overide method for class beagle'''
        return int(math.log(value) * 12 + 31)

class Dalmatian(Dog):
    '''Concrete class,  inherits from Pet'''

    def __init__(self, *args, **kwargs):
        '''Dalmatian constructor, takes a list and a dict as argument'''
        Dog.__init__(self, kwargs['name'], kwargs['age'], kwargs['weight'])
        self.height = kwargs['height']
        self.width = kwargs['width']
        self.colors = args
    def __str__(self):
        '''String representation of Dalmatian'''
        return '{:10}: {:s}'.format(Dog.__str__(self), 'Dalmatian')
    def _human_age(self, value):
        '''Overide method for class Dalmatian'''
        return int(math.log(value) * 20 + 31)

def main():
    '''Main program'''
    colors = (('black', 'white', 'brown'), ('black', 'white'), ('brown', 'white'))
    dog_dict1 = {'name':'snoop', 'age':3, 'weight':13, 'height':15, 'width':30}
    dog_dict2 = {'name':'jessy', 'age':2, 'weight':12, 'height':13, 'width':29}
    dog_dict3 = {'name':'stark', 'age':4, 'weight':14, 'height':15, 'width':31}
    dog_dict4 = {'name':'nebulosa', 'age':2, 'weight':12, 'height':13, 'width':28}
    dogs = [Beagle(*colors[2], **dog_dict1), Beagle(*colors[0], **dog_dict2),
        Dalmatian(*colors[1], **dog_dict3), Dalmatian(*colors[1], **dog_dict4)]
    
    for dog in dogs:
        print(dog, dog._human_age(dog.age), dog.colors, dog.food())

main()

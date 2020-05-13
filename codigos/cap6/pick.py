'''
How to program in Python - chapter 6
Class attribute example using class Pick
'''

class Pick:
    '''Represents a pick'''
    count = 0  # class attribute

    def __init__(self, size=0.5, color='red'):
        self.size = size
        self.color = color

        Pick.count += 1

        print('Pick{} with size {} and color {}'.format(Pick.count, self.size, self.color))

    def __del__(self):
        '''Decrements count and print messages'''
        Pick.count -= 1
        print('Decrementing pick counter using destructor')

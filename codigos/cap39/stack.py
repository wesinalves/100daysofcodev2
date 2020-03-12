"""
# Journey Python - Chapter 39
# Stack data structure implementation.
"""

class Stack:
    """class for stack structure"""
    def __init__(self, size=10):
        """Initialize stack"""
        self._top = 0
        self._array = [None] * size

    def stack_empty(self):
        """check if stack is empty"""
        if self._top == 0:
            return True
        else:
            return False
        

    def push(self, value):
        """Implement push operation"""
        self._top = self._top + 1
        if self._top == len(self._array):
            self._expand()

        self._array[self._top] = value

    def pop(self):
        """Implement pop operation"""
        if self.stack_empty():
            raise IndexError("Underflow!")
        else:
            value = self._array[self._top]
            self._array[self._top] = None
            self._top = self._top - 1
            return value
    
    def peek(self):
        """Returns the current top element"""
        if self.stack_empty():
            raise IndexError("Stack is empty")
        return self._array[self._top]
    
    def _expand(self):
        """private method to expand array"""
        self._array += [None] * len(self._array) # double the size of array

# Python Journey - Chapter 15
# Unsynchronized Integer Class

import threading

class UnsynchronizedInteger(threading.Thread):
    """Class that provides unsynchronized access an integer"""

    def __init__(self):
        """Initialize shared number to -1"""
        
        self.shared_number = -1
    
    def setSharedNumber(self, new_number):
        """Set value of integer"""

        print("%s setting sharedNumber to %d" %( threading.currentThread().getName(), new_number))
        self.shared_number = new_number
    
    def getSharedNumber(self):
        """Get value of integer"""

        temp = self.shared_number
        print("%s retrieving sharedNumber value %d" % (threading.currentThread().getName(), temp))

        return temp

'''
How to program in Python - Chapter 15
Synchronized access to an integer with condition variable
'''

import threading

class SynchronizedInteger:
    """Class that provides synchronized access an integer"""

    def __init__(self):
        """Set shared number, write flag and condition variable"""

        self.shared_number = -1
        self.writable = 1 # the value can be changed
        self.thread_condition = threading.Condition()

    def setSharedNumber(self, new_number):
        """Set value of integer--blocks until lock acquired"""

        self.thread_condition.acquire()

        # while not producer’s turn, release lock and block
        while not self.writable:
            self.thread_condition.wait()
        
        print("%s setting sharedNumber to %d" % (threading.currentThread().getName(), new_number))
        self.shared_number = new_number
        self.writable = 0
        self.thread_condition.notify()
        self.thread_condition.release()
    
    def getSharedNumber(self):
        """Get value of integer--blocks until lock acquired"""

        self.thread_condition.acquire()

        # while producer’s turn, release lock and block
        while self.writable:
            self.thread_condition.wait()
        
        # (lock has now been re-acquired)
        temp_number = self.shared_number
        print("%s retrieving sharedNumber value %d" % (threading.currentThread().getName(), temp_number))

        self.writable = 1
        self.thread_condition.notify()
        self.thread_condition.release()

        
        return temp_number
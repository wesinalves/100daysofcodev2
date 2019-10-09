# Python Journey - Chapter 15
# Synchronized circular buffer of integer values

import threading

class SynchronizedCells:
    """Set cells, flags, locations and condition variable"""
    def __init__(self):
        self.shared_cells = [ -1, -1, -1, -1, -1 ] # buffer
        self.writable = 1 # buffer may be changed
        self.readable = 0 # buffer may not be read
        self.write_location = 0 # current writing index
        self.read_location = 0 # current reading index

        self.thread_condition = threading.Condition()

    def setSharedNumber(self, new_number):
        """Set next buffer index value--blocks until lock acquired"""

        # block until lock released then acquire lock
        self.thread_condition.acquire()

        # while buffer is full, release lock and block
        while not self.writable:
            print("WAITING TO PRODUCE", new_number)
            self.thread_condition.wait()
        
        # buffer is not full, lock has been re-acquired

        # produce a number in shared cells, consumer may consume
        self.shared_cells[self.write_location] = new_number
        self.readable = 1
        print("Produced %2d into cell %d" % (new_number, self.write_location))

        # set writing index to next place in buffer
        self.write_location = (self.write_location + 1) % 5

        print(" write %d read %d " % (self.write_location, self.read_location))
        print(self.shared_cells)

        # if producer has caught up to consumer, buffer is full
        if self.write_location == self.read_location:
            self.writable = 0
            print("Buffer Full")
        
        self.thread_condition.notify()
        self.thread_condition.release()
    
    def getSharedNumber(self):
        """Get next buffer index value--blocks until lock acquired"""

        # block until lock released then acquire lock
        self.thread_condition.acquire()

        while not self.readable:
            print("WAITING TO CONSUME")
            self.thread_condition.wait()
        
        # buffer is not empty, lock has been re-acquired
        # consume a number from shared cells, producer may produce
        self.writable = 1
        temp = self.shared_cells[self.read_location]
        self.shared_cells[self.read_location] = -1

        print("Consumed %2d from cell %d" % (temp, self.read_location))

        # move to next produced number
        self.read_location = (self.read_location + 1) % 5

        print(" write %d read %d " % (self.write_location, self.read_location))
        print(self.shared_cells)

        # if consumer has caught up to producer, buffer is empty
        if self.read_location == self.write_location:
            self.readable = 0
            print("BUFFER EMPTY")
        
        self.thread_condition.notify()
        self.thread_condition.release()

        return temp




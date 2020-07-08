'''
How to program in Python - Chapter 15
Consume Integer Class
'''
import threading
import random
import time


class ConsumeInteger(threading.Thread):
    """Thread to consume integers"""

    def __init__(self, thread_name, shared_object):
        """Initialize thread, set shared object"""

        threading.Thread.__init__(self, name=thread_name)
        self.shared_object = shared_object

    def run(self):
        """Consume 10 values at random time intervals"""

        addition = 0

        # consume 10 values
        for _ in range(10):
            time.sleep(random.randrange(4))
            addition += self.shared_object.getSharedNumber()

        print("%s retrieved values totaling: %d" % (self.getName(), addition))
        print("Terminating", self.getName())

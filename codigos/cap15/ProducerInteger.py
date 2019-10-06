# Python Journey - Chapter 15
# Produce Integer Class

import threading
import random
import time

class ProduceInteger(threading.Thread):
    """Thread to produce integers"""

    def __init__(self, thread_name, shared_object):
        """Initialize thread, set shared object"""

        threading.Thread.__init__(self, name = thread_name)
        self.shared_object = shared_object
    
    def run(self):
        """Produce integers in range 1-10 at random intervals"""

        for i in range(1, 11):
            time.sleep(random.randrange(4))
            self.shared_object.setSharedNumber(1)
        
        print(self.getName(), "finished producing values")
        print("Terminating", self.getName())


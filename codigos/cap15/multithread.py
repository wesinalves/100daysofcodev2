# Python Journey - Chapter 15
# Show multiple threads printing at different intervals

import threading
import random
import time

class PrintThread(threading.Thread):
    """Subclass of threading.Thread"""

    def __init__(self, thread_name):
        """Initialize thread, set sleep time, print data"""

        threading.Thread.__init__(self, name = thread_name)
        self.sleep_time = random.randrange(1,6)
        print("Name: %s; sleep: %d" % (self.getName(), self.sleep_time))

    def run(self):
        """Sleep for 1-5 seconds"""

        print(self.getName())
        time.sleep(self.sleep_time)
        print(self.getName(), "done sleeping")
    

thread1 = PrintThread("thread1")
thread2 = PrintThread("thread2")
thread3 = PrintThread("thread3")
thread4 = PrintThread("thread4")

print("\nStarting threads")

thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("Threads started\n")




# Python Journey - Chapter 15
# Using a semaphore to control access to a critical section

import threading
import random
import time

class SemaphoreThread(threading.Thread):
    """Class using semaphores"""

    avaiable_tables = ["A", "B", "C", "D", "E"]

    def __init__(self, threading_name, semaphore):

        threading.Thread.__init__(self, name = threading_name)
        self.sleep_time = random.randrange(1,6)

        # set the semaphore as a data attribute of the class
        self.thread_sempaphore = semaphore

    def run(self):
        
        self.thread_sempaphore.acquire()
        
        # remove a table from the list
        table = SemaphoreThread.avaiable_tables.pop()

        print("%s entered; seated at table %s." % (self.getName(), table), end = "")
        print(SemaphoreThread.avaiable_tables)

        time.sleep(self.sleep_time)

        print("%s exiting; freeing table %s." % (self.getName(), table), end = "")
        SemaphoreThread.avaiable_tables.append(table)
        print(SemaphoreThread.avaiable_tables)

        # release the semaphore after execution finishes
        self.thread_sempaphore.release()

threads = []

# semaphore allows five threads to enter critical section
thread_semaphore = threading.Semaphore(len(SemaphoreThread.avaiable_tables))

# create ten threads
for i in range(1,11):
    threads.append(SemaphoreThread("Thread" + str(i), thread_semaphore))

# start each thread
for thread in threads:
    thread.start()


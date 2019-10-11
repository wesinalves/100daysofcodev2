# Python Journey - Chapter 15
# Demonstrating event objetc

import threading
import random
import time

class VehicleThread(threading.Thread):
    """Class representing a motor vehicle at an intersection"""

    def __init__(self, thread_name, event):
        """Initializes thread"""

        threading.Thread.__init__(self, name = thread_name)
        self.thread_event = event

    
    def run(self):
        """Vehicle waits unless/until light is green"""

        time.sleep(random.randrange(1,10))

        print("%s arrived at %s" % (self.getName(), time.ctime(time.time())))

        self.thread_event.wait()

        print("%s passes through intersection at %s" % (self.getName(), time.ctime(time.time())))

green_light = threading.Event()
vehicle_threads = []

# creates and starts ten Vehicle threads
for i in range(1,11):
    vehicle_threads.append(VehicleThread("Vehicle" + str(i), green_light))

# start each thread
for thread in vehicle_threads:
    thread.start()

while threading.activeCount() > 1:
    # sets the Event object’s flag to false
    green_light.clear()
    print("RED LIGHT")

    time.sleep(3)

    # sets the Event object’s flag to true
    print("GREEN LIGHT")
    green_light.set()

    time.sleep(2)

    
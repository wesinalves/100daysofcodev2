# Python Journey - Chapter 15
# Show multiple threads modifying shared object

from SynchronizedInteger import SynchronizedInteger
from ProduceInteger import ProduceInteger
from ConsumeInteger import ConsumeInteger

# initialize integer and threads
number = SynchronizedInteger()
producer = ProduceInteger("Producer", number)
consumer = ConsumeInteger("Consumer", number)

print("Start threads...\n")

producer.start()
consumer.start()

# wait for threads to terminate
producer.join()
consumer.join()

print("\nAll threads have terminated.")
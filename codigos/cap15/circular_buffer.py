'''
How to program in Python - Chapter 15
Show multiple threads modifying shared object
'''

from SynchronizedCells import SynchronizedCells
from ProduceInteger import ProduceInteger
from ConsumeInteger import ConsumeInteger


def main():
    '''initialize integer and threads'''
    number = SynchronizedCells()
    producer = ProduceInteger("Producer", number)
    consumer = ConsumeInteger("Consumer", number)

    print("Start threads...\n")

    producer.start()
    consumer.start()

    # wait for threads to terminate
    producer.join()
    consumer.join()

    print("\nAll threads have terminated.")

main()

'''
How to program in Python - Chapter 5
Creating and accessing tuples.
'''

def time_tuple():
    '''Creating Tuple'''
    # retrieve hour, minute and second from user
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    second = int(input("Enter second: "))

    current_time = hour, minute, second  # create tuple

    print("The value of current_time is:", current_time)

    # access tuple
    print("The number of seconds since midnight is", \
        (current_time[0] * 3600 + current_time[1] * 60 + \
        current_time[2]))

time_tuple()

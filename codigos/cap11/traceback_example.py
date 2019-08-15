# Python Journey - Chapter 11
# Demonstrating exception arguments and stack unwinding.

import traceback

def function1():
    function2()

def function2():
    function3()

def function3():

    # raise exception, catch exception, reraise exception
    try:
        raise Exception("An exception has occurred")
    except Exception:
        print("Caught exception in function3. Reraising....\n")
        raise

try:
    function1()
except Exception as exception:
    print("Exception caught in main program.")
    print("\nException arguments:", exception.args)
    print("\nException message:", exception)    
    traceback.print_exec()
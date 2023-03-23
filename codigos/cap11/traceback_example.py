'''
How to program in Python - Chapter 11
Demonstrating exception arguments and stack unwinding.
'''
import traceback

def function1():
    '''this is function 1'''
    function2()

def function2():
    '''this is function2'''
    function3()

def function3():
    '''raise exception, catch exception, reraise exception'''
    try:
        raise Exception("An exception has occurred", "second argument")
    except Exception:
        print("Caught exception in function3. Reraising....\n")
        raise

def main():
    '''Main Program'''
    try:
        function1()
    except Exception as e:
        traceback.print_exc()
        print("Exception caught in main program.")
        print("\nException arguments:", e.args)
        print("\nException message:", e)    

if __name__ == '__main__':
    main()

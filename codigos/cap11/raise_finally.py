'''
How to program in Python - Chapter 11
Using finally clauses.
'''

def doNotRaiseException():
    '''try block does not raise any exceptions'''
    try:
        print("In doNotRaiseException()")

    # finally executes because corresponding try executed
    finally:
        print("Finally executed in doNotRaiseException")

    print("End of doNotRaiseException")

def raiseExceptionDoNotCatch():
    '''raise exception, but do not catch it'''
    try:
        print("In raiseExceptionDoNotCatch()")
        raise Exception
        return
    # finally executes because corresponding try executed
    finally:
        print("Finally executed in raiseExceptionDoNotCatch")
        return
        
        
        
    
    print("Will never reach this point")

def main():
    '''Main Program'''
    # case 1: no exceptions occurs in called function
    doNotRaiseException()

    # case2: Exception occurs, but is not handled in called function,
    # because no except clauses exist in raiseExceptionDoNotCatch

    try:
        raiseExceptionDoNotCatch()

    except Exception:
        print("Caught exception from raiseExceptionDoNotCatch")
               


if __name__ == '__main__':
    main()

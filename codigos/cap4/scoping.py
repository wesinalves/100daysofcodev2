'''
How to program in Python - Chapter 4
Scoping example
'''

NUMBER = 1

def local_scope():
    '''check local scope'''
    NUMBER = 25

    print('Local NUMBER in local_scope is', NUMBER, 'after entering local_scope')
    NUMBER += 1
    print('Local NUMBER in local_scope is', NUMBER, 'before exiting local_scope')

def global_scope():
    '''check global scope'''
    global NUMBER

    print('GLOBAL NUMBER in global_scope is', NUMBER, 'after entering global_scope')
    NUMBER *= 10
    print('GLOBAL NUMBER in global_scope is', NUMBER, 'before exiting global_scope')

print('global NUMBER is', NUMBER)

NUMBER = 7

print('global NUMBER is', NUMBER)

local_scope()
global_scope()
local_scope()
global_scope()

print('global NUMBER is', NUMBER)

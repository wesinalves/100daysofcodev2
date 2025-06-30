# Python program to demonstrate
# higher order functions

def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a \
                    function passed as an argument.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)
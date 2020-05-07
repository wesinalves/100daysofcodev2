'''
How to program in Python - Chapter 5
Avoiding duplicated words.
'''

def main():
    '''Main program'''
    fruits = set()
    fruit = input('Enter a fruit (blank line to exit)')
    while fruit != '':
        if fruit not in fruits:
            fruits.add(fruit)
        fruit = input('Enter a fruit (blank line to exit)')
    for item in fruits:
        print(item, end=',')

main()

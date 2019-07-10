def fibonacci(number):

    if number < 0:
        print('Valor negativo é invalido')
    
    if number == 0 or number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

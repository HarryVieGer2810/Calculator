import math

OPERATION = input('Choose your operation to perform: ')

if OPERATION == 'simple':
    print('1. ADDITION (+)')
    print('2. SUBTRACTION (-)')
    print('3. MULTIPLICATION (×)')
    print('4. DIVISION (÷)')
    operation = input('Select an operations to perform: ')
    if operation == '1': # ADDITION
        x = input('Enter your first number: ')
        y = input('Enter your second number: ')
        print('Sum is ' + str(int(x) + int(y)))
    elif operation == '2': # SUBTRACTION
        x = input('Enter your first number: ')
        y = input('Enter your second number: ')
        print('Difference is ' + str(int(x) - int(y)))
    elif operation == '3': # MULTIPLICATION
        x = input('Enter your first number: ')
        y = input('Enter your second number: ')
        print('Result is ' + str(int(x) * int(y)))
    elif operation == '4': # DIVISION
        x = input('Enter your first number: ')
        y = input('Enter your second number: ')
        print('Result is ' + str(int(x) / int(y)))
    else:
        quit()
elif OPERATION == 'sqrt':
    print('1. Square Root')
    print('2. X to the power of Y')

    operation = input('Select an operations to perform: ')

    if operation == '1': # Square Root
        x = int(input('Enter your number: '))
        print('Quare Root of ' + str(x) + ' is ' + str(math.sqrt(x)))
    elif operation == '2': # X to the power of Y
        x = int(input('Enter your number: '))
        y = int(input('Enter your number: '))
        print('Quare Root of ' + str(x) + ' to the power of ' + str(y) + ' is ' + str(math.pow(x, y)))
    else:
        quit()
elif OPERATION == 'sine':
    print('1. SINE')
    print('2. COS')
    print('3. TAN')
    print('4. COTAN')

    operation = input('Select an operations to perform: ')

    if operation == '1':
        a = eval(input('what is the angle measure?'))
        result = math.sin(math.radians(a))
        print('the answer is' + str(round(result, 3)))
    elif operation == '2':
        a = eval(input('what is the angle measure?'))
        result = math.cos(math.radians(a))
        print('the answer is' + str(round(result, 3)))
    elif operation == '3':
        a = eval(input('what is the angle measure?'))
        result = math.tan(math.radians(a))
        print('the answer is' + str(round(result, 3)))
    else:
        print('Other operations:')
else:
    quit()

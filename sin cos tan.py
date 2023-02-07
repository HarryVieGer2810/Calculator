import math
print('1. SIN')
print('2. COS')
print('3. TAN')

operation = input('Select an operations to perform: ')
if operation == '1':
        a= eval(input('what is the angle measure?'))
        result = math.sin(math.radians(a))
        print('the answer is'+ str(round(result, 3)))
elif operation == '2':
        a= eval(input('what is the angle measure?'))
        result = math.cos(math.radians(a))
        print('the answer is'+ str(round(result, 3)))
elif operation == '3':
        a= eval(input('what is the angle measure?'))
        result = math.tan(math.radians(a))
        print('the answer is'+ str(round(result, 3)))

else:
    print('Other operations:')

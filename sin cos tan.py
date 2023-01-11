import math
trig = input('do you want to calculate sin, cos, tan?')
if trig == 'cos':
        a= eval(input('what is the angle measure?'))
        result = math.cos(math.radians(a))
        print('the answer is'+ str(round(result, 3)))
elif trig == 'tan':
        a= eval(input('what is the angle measure?'))
        result = math.tan(math.radians(a))
        print('the answer is'+ str(round(result, 3)))
elif trig == 'sin':
        a= eval(input('what is the angle measure?'))
        result = math.sin(math.radians(a))
        print('the answer is'+ str(round(result, 3)))

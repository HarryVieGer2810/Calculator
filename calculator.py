import tkinter as calculator
import math

# ##############################################################################################

container = calculator.Tk()
container.geometry('300x500')
container.title('Calculator')

lable = calculator.Label(container, text="SMC - 11A1", font=('Arial', 20))
lable.pack(padx=20, pady=20)

display = calculator.Text(container, height=3, font=('Arial', 15))
display.pack(padx=10, pady=10)

buttonFrame = calculator.Frame(container)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
button1 = calculator.Button(buttonFrame, text='AC', font=('Arial', 10))
button1.grid(row=0, column=0, sticky=calculator.W+calculator.E)
button2 = calculator.Button(buttonFrame, text='DE', font=('Arial', 10))
button2.grid(row=0, column=1, sticky=calculator.W+calculator.E)
button3 = calculator.Button(buttonFrame, text='ANS', font=('Arial', 10))
button3.grid(row=0, column=2, sticky=calculator.W+calculator.E)
# button4 = calculator.Button(buttonFrame, text='/', font=('Arial', 10))
# button4.grid(row=0, column=3, sticky=calculator.W+calculator.E)

buttonFrame.pack(fill='x')

container.mainloop()

# ##############################################################################################
print('Select an operations to perform: ')
print('1. ADDITION (+)')
print('2. SUBTRACTION (-)')
print('3. MULTIPLICATION (×)')
print('4. DIVISION (÷)')

operation = input('Select an operations to perform: ')

# Simple operations
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
    print('Other operations: ')

# Other
print('1. Square Root')
print('2. X to the power of Y')
print('3. ')
print('4. Cubed X^3')

operation = input('Select an operations to perform: ')

if operation == '1': # Square Root
    x = int(input('Enter your number: '))
    print('Quare Root of ' + str(x) + ' is ' + str(math.sqrt(x)))
elif operation == '2': # X to the power of Y
    x = int(input('Enter your number: '))
    y = int(input('Enter your number: '))
    print('Quare Root of ' + str(x) + ' to the power of ' + str(y) + ' is ' + str(math.pow(x, y)))
else:
    print('Other operations: ')

# COSINE
print('1. SINE')
print('2. COS')
print('3. TAN')
print('4. COTAN')

operation = input('Select an operations to perform: ')

if operation == '1': # SIN MOTHOD
    # x = int(input('Enter your number (SIN): '))
    # print('SIN(' + str(x) + ') ' + 'is ' + str(math.sin(x)))
    x = eval(input('what is the angle measure?'))
    result = math.cos(math.radians(x))
    print('SIN(' + str(x) + ') ' + 'is ' + str(round(result, 3)))
elif operation == '2': # COS METHOD
    x = int(input('Enter your number (COS): '))
    print('COS(' + str(x) + ') ' + 'is ' + str(math.cos(x)))
elif operation == '3':  # TAN METHOD
    x = int(input('Enter your number (TAN): '))
    print('TAN(' + str(x) + ') ' + 'is ' + str(math.tan(x)))
else:
    print('Other operations:')

# Length

print('1. CM -> IN')
print('2. IN -> CM')
print('3. M -> FT')
print('4. FT -> M')
print('5. M -> YD')
print('6. YD -> M')
print('7. KM -> MILE')
print('8. MILE -> KM')

operation = input('Select an operations to perform: ')

if operation == '1': # CM -> IN
    CM = int(input('Enter your number (CM -> IN): '))
    IN = int(CM) / 2.54
    print(str(CM) + ' CM ' + '= ' + str(IN) + ' IN')
elif operation == '2': # IN -> CM
    IN = int(input('Enter your number (IN -> CM): '))
    CM = int(IN) * 2.54
    print(str(IN) + ' IN ' + '= ' + str(CM) + ' CM')
elif operation == '3': # M -> FT
    M = int(input('Enter your number (M -> FT): '))
    FT = int(M) / 0.3048
    print(str(M) + ' M ' + '= ' + str(FT) + ' FT')
elif operation == '4': # FT -> M
    FT = int(input('Enter your number (FT -> M): '))
    M = int(FT) * 0.3048
    print(str(FT) + ' FT ' + '= ' + str(M) + ' M')
elif operation == '5': # M -> YD
    M = int(input('Enter your number (M -> YD): '))
    YD = int(M) / 0.3048
    print(str(M) + ' M ' + '= ' + str(YD) + ' YD')
elif operation == '6': # YD -> M
    YD = int(input('Enter your number (YD -> M): '))
    M = int(YD) * 0.3048
    print(str(YD) + ' YD ' + '= ' + str(M) + ' M')
elif operation == '6':  # YD -> M
    YD = int(input('Enter your number (YD -> M): '))
    M = int(YD) * 0.3048
    print(str(YD) + ' YD ' + '= ' + str(M) + ' M')

# import tkinter

import tkinter as tk

calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')



root = tk.Tk()
root.geometry('500x500')

text_result = tk.Text(root, height=2, width=16, font=('Arial', 25))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=2, font=('Arial', 15))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=2, font=('Arial', 15))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=2, font=('Arial', 15))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=2, font=('Arial', 15))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=2, font=('Arial', 15))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=2, font=('Arial', 15))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=2, font=('Arial', 15))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=2, font=('Arial', 15))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=2, font=('Arial', 15))
btn_9.grid(row=4, column=3)
btn_open = tk.Button(root, text='(', command=lambda: add_to_calculation('('), width=2, font=('Arial', 15))
btn_open.grid(row=5, column=1)
btn_0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=2, font=('Arial', 15))
btn_0.grid(row=5, column=2)
btn_close = tk.Button(root, text=')', command=lambda: add_to_calculation(')'), width=2, font=('Arial', 15))
btn_close.grid(row=5, column=3)
btn_addition = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=2, font=('Arial', 15))
btn_addition.grid(row=2, column=4)
btn_subtraction = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=2, font=('Arial', 15))
btn_subtraction.grid(row=3, column=4)
btn_multiplication = tk.Button(root, text='*', command=lambda: add_to_calculation('*'), width=2, font=('Arial', 15))
btn_multiplication.grid(row=4, column=4)
btn_division = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=2, font=('Arial', 15))
btn_division.grid(row=5, column=4)
btn_clear = tk.Button(root, text='AC', command=lambda: clear_field, width=11, font=('Arial', 15))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equal = tk.Button(root, text='=', command=lambda: evaluate_calculation(), width=11, font=('Arial', 15))
btn_equal.grid(row=6, column=3, columnspan=2)

root.mainloop()

# lable = calculator.Label(container, text="SMC - 11A1", font=('Arial', 20))
# lable.pack(padx=20, pady=20)
#
# display = calculator.Text(container, height=3, font=('Arial', 15))
# display.pack(padx=10, pady=10)
#
# buttonFrame = calculator.Frame(container)
# buttonFrame.columnconfigure(0, weight=1)
# buttonFrame.columnconfigure(1, weight=1)
# buttonFrame.columnconfigure(2, weight=1)
# buttonFrame.columnconfigure(3, weight=1)
#
# button1 = calculator.Button(buttonFrame, text='7', font=('Arial', 10))
# button1.grid(row=0, column=0)
# button2 = calculator.Button(buttonFrame, text='8', font=('Arial', 10))
# button2.grid(row=0, column=1)
# button3 = calculator.Button(buttonFrame, text='9', font=('Arial', 10))
# button3.grid(row=0, column=2)
# buttonMultiplication = calculator.Button(buttonFrame, text='*', font=('Arial', 10))
# buttonMultiplication.grid(row=0, column=3)
#
# buttonFrame.pack(fill='x')
#
# container.mainloop()

# ##############################################################################################
# print('Select an operations to perform: ')
# print('1. ADDITION (+)')
# print('2. SUBTRACTION (-)')
# print('3. MULTIPLICATION (×)')
# print('4. DIVISION (÷)')
#
# operation = input('Select an operations to perform: ')
#
# # Simple operations
# if operation == '1': # ADDITION
#     x = input('Enter your first number: ')
#     y = input('Enter your second number: ')
#     print('Sum is ' + str(int(x) + int(y)))
# elif operation == '2': # SUBTRACTION
#     x = input('Enter your first number: ')
#     y = input('Enter your second number: ')
#     print('Difference is ' + str(int(x) - int(y)))
# elif operation == '3': # MULTIPLICATION
#     x = input('Enter your first number: ')
#     y = input('Enter your second number: ')
#     print('Result is ' + str(int(x) * int(y)))
# elif operation == '4': # DIVISION
#     x = input('Enter your first number: ')
#     y = input('Enter your second number: ')
#     print('Result is ' + str(int(x) / int(y)))
# else:
#     print('Other operations: ')
#
# # Other
# print('1. Square Root')
# print('2. X to the power of Y')
# print('3. ')
# print('4. Cubed X^3')
#
# operation = input('Select an operations to perform: ')
#
# if operation == '1': # Square Root
#     x = int(input('Enter your number: '))
#     print('Quare Root of ' + str(x) + ' is ' + str(math.sqrt(x)))
# elif operation == '2': # X to the power of Y
#     x = int(input('Enter your number: '))
#     y = int(input('Enter your number: '))
#     print('Quare Root of ' + str(x) + ' to the power of ' + str(y) + ' is ' + str(math.pow(x, y)))
# else:
#     print('Other operations: ')
#
# # COSINE
# print('1. SINE')
# print('2. COS')
# print('3. TAN')
# print('4. COTAN')
#
# operation = input('Select an operations to perform: ')
#
# if operation == '1': # SIN MOTHOD
#     # x = int(input('Enter your number (SIN): '))
#     # print('SIN(' + str(x) + ') ' + 'is ' + str(math.sin(x)))
#     x = eval(input('what is the angle measure?'))
#     result = math.cos(math.radians(x))
#     print('SIN(' + str(x) + ') ' + 'is ' + str(round(result, 3)))
# elif operation == '2': # COS METHOD
#     x = int(input('Enter your number (COS): '))
#     print('COS(' + str(x) + ') ' + 'is ' + str(math.cos(x)))
# elif operation == '3':  # TAN METHOD
#     x = int(input('Enter your number (TAN): '))
#     print('TAN(' + str(x) + ') ' + 'is ' + str(math.tan(x)))
# else:
#     print('Other operations:')
#
# # Length
#
# print('1. CM -> IN')
# print('2. IN -> CM')
# print('3. M -> FT')
# print('4. FT -> M')
# print('5. M -> YD')
# print('6. YD -> M')
# print('7. KM -> MILE')
# print('8. MILE -> KM')
#
# operation = input('Select an operations to perform: ')
#
# if operation == '1': # CM -> IN
#     CM = int(input('Enter your number (CM -> IN): '))
#     IN = int(CM) / 2.54
#     print(str(CM) + ' CM ' + '= ' + str(IN) + ' IN')
# elif operation == '2': # IN -> CM
#     IN = int(input('Enter your number (IN -> CM): '))
#     CM = int(IN) * 2.54
#     print(str(IN) + ' IN ' + '= ' + str(CM) + ' CM')
# elif operation == '3': # M -> FT
#     M = int(input('Enter your number (M -> FT): '))
#     FT = int(M) / 0.3048
#     print(str(M) + ' M ' + '= ' + str(FT) + ' FT')
# elif operation == '4': # FT -> M
#     FT = int(input('Enter your number (FT -> M): '))
#     M = int(FT) * 0.3048
#     print(str(FT) + ' FT ' + '= ' + str(M) + ' M')
# elif operation == '5': # M -> YD
#     M = int(input('Enter your number (M -> YD): '))
#     YD = int(M) / 0.3048
#     print(str(M) + ' M ' + '= ' + str(YD) + ' YD')
# elif operation == '6': # YD -> M
#     YD = int(input('Enter your number (YD -> M): '))
#     M = int(YD) * 0.3048
#     print(str(YD) + ' YD ' + '= ' + str(M) + ' M')
# elif operation == '6':  # YD -> M
#     YD = int(input('Enter your number (YD -> M): '))
#     M = int(YD) * 0.3048
#     print(str(YD) + ' YD ' + '= ' + str(M) + ' M')

######################################           GUI based Calculator in Python               ###################################

import tkinter as tk

# Functions for calculator operations
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result: " + str(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        label_result.config(text="Cannot divide by zero")
    else:
        result = num1 / num2
        label_result.config(text="Result: " + str(result))

# Create a GUI window
calculator = tk.Tk()
calculator.geometry('500x300+200+150')

calculator.title("CALCULATOR")
calculator.resizable(False,False)

# Create input fields for numbers
label1 = tk.Label(calculator, text="Enter first number:",font=('arial',10,'italic bold'))
label1.pack()
entry1 = tk.Entry(calculator,font=('arial',10,'italic bold'),width=40)
entry1.pack()

label2 = tk.Label(calculator, text="Enter second number:",font=('arial',10,'italic bold'))
label2.pack()
entry2 = tk.Entry(calculator,font=('arial',10,'italic bold'),width=40)
entry2.pack()

# Create buttons for calculator operations
button_add = tk.Button(calculator, text="+",bg='Light Blue', command=add, width=10, height=2)
button_add.pack()

button_subtract = tk.Button(calculator, text="-",bg='Light Blue', command=subtract, width=10, height=2)
button_subtract.pack()

button_multiply = tk.Button(calculator, text="*",bg='Light Blue', command=multiply, width=10, height=2)
button_multiply.pack()

button_divide = tk.Button(calculator, text="/",bg='Light Blue', command=divide, width=10, height=2)
button_divide.pack()

# Create a label to display the result
label_result = tk.Label(calculator, text="Result:",bg= 'Red',font=('arial',15,'italic bold'))
label_result.pack()

# Run the GUI
calculator.mainloop()

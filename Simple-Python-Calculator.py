from tkinter import *
import math

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Undefined")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def erase():
    global equation_text
    equation_text = equation_text[:-1]  # Remove the last character
    equation_label.set(equation_text)

def calculate_square():
    global equation_text
    try:
        num = float(equation_text)
        result = num ** 2
        equation_label.set(result)
        equation_text = str(result)
    except ValueError:
        equation_label.set("Invalid input for square")
        equation_text = ""

def calculate_square_root():
    global equation_text
    try:
        num = float(equation_text)
        result = math.sqrt(num)
        equation_label.set(result)
        equation_text = str(result)
    except ValueError:
        equation_label.set("Invalid input for square root")
        equation_text = ""

window = Tk()
window.title("Group 2's Calculator!")
window.geometry("550x640")
window.configure(bg='black')

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Tahoma', 20), bg="white", fg="black", width=31, height=3)
label.pack(pady=10)

frame = Frame(window, bg='black')
frame.pack()

# Numeric buttons
button1 = Button(frame, text=1, height=3, width=9, font=35, command=lambda: button_press(1), bg='dark gray', fg='white')
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(frame, text=2, height=3, width=9, font=35, command=lambda: button_press(2), bg='dark gray', fg='white')
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(frame, text=3, height=3, width=9, font=35, command=lambda: button_press(3), bg='dark gray', fg='white')
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(frame, text=4, height=3, width=9, font=35, command=lambda: button_press(4), bg='dark gray', fg='white')
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(frame, text=5, height=3, width=9, font=35, command=lambda: button_press(5), bg='dark gray', fg='white')
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(frame, text=6, height=3, width=9, font=35, command=lambda: button_press(6), bg='dark gray', fg='white')
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(frame, text=7, height=3, width=9, font=35, command=lambda: button_press(7), bg='dark gray', fg='white')
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(frame, text=8, height=3, width=9, font=35, command=lambda: button_press(8), bg='dark gray', fg='white')
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(frame, text=9, height=3, width=9, font=35, command=lambda: button_press(9), bg='dark gray', fg='white')
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(frame, text=0, height=3, width=9, font=35, command=lambda: button_press(0), bg='dark gray', fg='white')
button0.grid(row=4, column=0, padx=5, pady=5)

# Operator buttons
plus = Button(frame, text='+', height=3, width=9, font=35, command=lambda: button_press('+'), bg='orange')
plus.grid(row=1, column=3, padx=5, pady=5)

minus = Button(frame, text='-', height=3, width=9, font=35, command=lambda: button_press('-'), bg='orange')
minus.grid(row=2, column=3, padx=5, pady=5)

multiply = Button(frame, text='x', height=3, width=9, font=35, command=lambda: button_press('*'), bg='orange')
multiply.grid(row=3, column=3, padx=5, pady=5)

divide = Button(frame, text='÷', height=3, width=9, font=35, command=lambda: button_press('/'), bg='orange')
divide.grid(row=4, column=3, padx=5, pady=5)

equal = Button(frame, text='=', height=3, width=9, font=35, command=equals, bg='orange')
equal.grid(row=4, column=2, padx=5, pady=5)

decimal = Button(frame, text='.', height=3, width=9, font=35, command=lambda: button_press('.'), bg='dark gray', fg='white')
decimal.grid(row=4, column=1, padx=5, pady=5)

# Special buttons
erase_button = Button(frame, text='<<<', height=3, width=9, font=35, command=erase, bg='gray')
erase_button.grid(row=0, column=1, padx=5, pady=5)

square_button = Button(frame, text='x²', height=3, width=9, font=35, command=calculate_square, bg='gray')
square_button.grid(row=0, column=2, padx=5, pady=5)

square_root_button = Button(frame, text='√x', height=3, width=9, font=35, command=calculate_square_root, bg='orange')
square_root_button.grid(row=0, column=3, padx=5, pady=5)

clear_button = Button(frame, text='C', height=3, width=9, font=35, command=clear, bg='gray')
clear_button.grid(row=0, column=0, padx=5, pady=5)

window.mainloop()
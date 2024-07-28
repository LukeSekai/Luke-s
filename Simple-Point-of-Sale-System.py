from tkinter import *

def food(row, column, selected_items, receipt):
    food1 = [["Burger", "Fries", "Chicken w Rice"],
             ["Palabok", "Spaghetti", "Chic Fillet"],
             ["Burger Steak", "Chicken w Burger", "Spaghetti w Burger"]]
    
    food_Price = {"Burger": 60, "Fries": 59, "Chicken w Rice": 120,
                  "Palabok": 119, "Spaghetti": 79, "Chic Fillet": 79,
                  "Burger Steak": 89, "Chicken w Burger": 109, "Spaghetti w Burger": 99}
    
    selected_food = food1[row][column]
    Fprice = food_Price[selected_food]

    selected_items.append((selected_food, Fprice))
    update_receipt(selected_items, receipt)

def drinks(row, column, selected_items, receipt):
    drink1 = [["Cola", "Sprite", "Pepsi"],
              ["Water", "Juice", "Iced tea"]]
    
    drink_price = {"Cola": 40, "Sprite": 40, "Pepsi": 40,
                   "Water": 10, "Juice": 20, "Iced tea": 30}
    
    selected_drink = drink1[row][column]
    Dprice = drink_price[selected_drink]

    selected_items.append((selected_drink, Dprice))
    update_receipt(selected_items, receipt)

def update_receipt(selected_items, receipt):
    receipt.config(state=NORMAL)
    receipt.delete(1.0, "end")
    receipt.insert("end", "Earls Eatery\n\n")
    
    total_cost = sum(price for _, price in selected_items)
    for item, price in selected_items:
        receipt.insert("end", item + ": ₱" + str(round(price, 2)) + "\n")

    receipt.insert("end", "\n\nTotal cost: ₱" + str(round(total_cost, 2)) + "\n")    
    receipt.config(state=DISABLED)

def clear_order(selected_items, receipt):
    global is_discounted_customer  # Add this line to access the global variable

    selected_items.clear()
    update_receipt(selected_items, receipt)

    # Reset the total cost and change labels
    total_cost_label.config(text="Total cost: ₱0.00")
    change_label.config(text="Change: ₱0.00")

    # Reset the change display receipt
    change_display_receipt.config(state=NORMAL)
    change_display_receipt.delete(1.0, "end")
    change_display_receipt.insert("end", "Change: ₱0.00")
    change_display_receipt.config(state=DISABLED)

    # Disable the PWD discount
    is_discounted_customer = False
    discount_button.config(state=DISABLED)

def delete_item(selected_items, receipt):
    index = int(entry.get()) - 1
    if 0 <= index < len(selected_items):
        del selected_items[index]
        update_receipt(selected_items, receipt)

def calculate_change(total_cost, payment_amount):
    return payment_amount - total_cost

def apply_discount(total_cost, is_discounted_customer):
    discount_rate = 0.20  # 20% discount
    if is_discounted_customer:
        return total_cost * (1 - discount_rate)
    else:
        return total_cost
    
def toggle_discount():
    global is_discounted_customer
    is_discounted_customer = not is_discounted_customer

    # Calculate the discounted cost
    total_cost = sum(price for _, price in selected_items)
    discounted_cost = apply_discount(total_cost, is_discounted_customer)

    # Update the total cost label with the discounted cost
    total_cost_label.config(text="Total cost after discount: ₱%.2f" % discounted_cost)

    # Recalculate the change
    payment_amount = float(payment_entry.get())
    change = calculate_change(discounted_cost, payment_amount)

    # Update the change label
    change_label.config(text="Change: ₱%.2f" % change)

    # Update the receipt and change display receipt
    receipt.config(state=NORMAL)
    receipt.delete("end-2l", "end")  # Delete the last two lines, which include the total cost and the empty line
    receipt.insert("end", "\nPayment: ₱%.2f\n" % payment_amount)
    receipt.insert("end", "Change: ₱%.2f\n" % change)
    receipt.config(state=DISABLED)

    change_display_receipt.config(state=NORMAL)
    change_display_receipt.delete(1.0, "end")
    change_display_receipt.insert("end", "Change: ₱%.2f\n" % change)
    change_display_receipt.config(state=DISABLED)

# Clear function for the C button
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""
    payment_entry.delete(0, END)  # Clear payment entry as well

# Pay function for the Pay button
def pay_and_change(selected_items, payment_entry, change_label, receipt, change_display_receipt, is_discounted_customer):
    payment_amount = float(payment_entry.get())
    total_cost = sum(price for _, price in selected_items)

    # Check if the payment is less than the total cost
    if payment_amount < total_cost:
        # Append a message saying "Insufficient payment" to the receipt
        receipt.config(state=NORMAL)
        receipt.insert("end", "\nInsufficient payment")
        receipt.config(state=DISABLED)
        return  # Exit the function

    # If payment is sufficient, clear the error message
    receipt.config(state=NORMAL)
    receipt.delete(1.0, "end")
    update_receipt(selected_items, receipt)  # Update the receipt here

    # Update the total cost label
    total_cost_label.config(text="Total cost: ₱%.2f" % total_cost)

    # Enable the discount button
    discount_button.config(state=NORMAL)

    discounted_cost = apply_discount(total_cost, is_discounted_customer)
    change = calculate_change(discounted_cost, payment_amount)

    # Update change label
    change_label.config(text="Change: ₱%.2f" % change)

    # Update receipt
    receipt.config(state=NORMAL)
    receipt.delete("end-2l", "end")  # Delete the last two lines, which include the total cost and the empty line
    receipt.insert("end", "\nPayment: ₱%.2f\n" % payment_amount)
    receipt.insert("end", "Change: ₱%.2f\n" % change)
    receipt.config(state=DISABLED)

    # Update change display receipt
    change_display_receipt.config(state=NORMAL)
    change_display_receipt.delete(1.0, "end")
    change_display_receipt.insert("end", "Change: ₱%.2f\n" % change)
    change_display_receipt.config(state=DISABLED)

# Calculator Functions
def update_payment_entry(num):
    current_payment = payment_entry.get()
    payment_entry.delete(0, END)
    payment_entry.insert(0, current_payment + str(num))

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    update_payment_entry(num)  # Add this line to update the payment entry

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
    payment_entry.delete(0, END)  # Clear payment entry as well

def erase():
    global equation_text
    equation_text = equation_text[:-1]  # Remove the last character
    equation_label.set(equation_text)
    current_payment = payment_entry.get()
    payment_entry.delete(0, END)
    payment_entry.insert(0, current_payment[:-1])  # Remove the last character from payment entry

window = Tk()
window.title("EARL'S EATERY")
window.geometry("900x950")

receipt = Text(window, font=('Helvetica', 16), bg="white", fg="black", width=21, height=20)
receipt.pack(side=RIGHT, anchor=NE, padx=20, pady=20)
receipt.config(state=DISABLED)

frame_food = Frame(window, bg='white')
frame_food.pack()

selected_items = []

# Food buttons
frame_food = Frame(window, bg='white')
frame_food.pack()

food1 = Button(frame_food, text="Burger", height=4, width=15, font=('Helvetica', 12), command=lambda: food(0, 0, selected_items, receipt), bg='#ff9999', fg='black')
food1.grid(row=0, column=0, padx=10, pady=10)

food2 = Button(frame_food, text="Fries", height=4, width=15, font=('Helvetica', 12), command=lambda: food(0, 1, selected_items, receipt), bg='#ff9999', fg='black')
food2.grid(row=0, column=1, padx=10, pady=10)

food3 = Button(frame_food, text="Chicken w Rice", height=4, width=15, font=('Helvetica', 12), command=lambda: food(0, 2, selected_items, receipt), bg='#ff9999', fg='black')
food3.grid(row=0, column=2, padx=10, pady=10)

food4 = Button(frame_food, text="Palabok", height=4, width=15, font=('Helvetica', 12), command=lambda: food(1, 0, selected_items, receipt), bg='#ff9999', fg='black')
food4.grid(row=1, column=0, padx=10, pady=10)

food5 = Button(frame_food, text="Spaghetti", height=4, width=15, font=('Helvetica', 12), command=lambda: food(1, 1, selected_items, receipt), bg='#ff9999', fg='black')
food5.grid(row=1, column=1, padx=10, pady=10)

food6 = Button(frame_food, text="Chicken Fillet", height=4, width=15, font=('Helvetica', 12), command=lambda: food(1, 2, selected_items, receipt), bg='#ff9999', fg='black')
food6.grid(row=1, column=2, padx=10, pady=10)

food7 = Button(frame_food, text="Burger Steak", height=4, width=15, font=('Helvetica', 12), command=lambda: food(2, 0, selected_items, receipt), bg='#ff9999', fg='black')
food7.grid(row=2, column=0, padx=10, pady=10)

food8 = Button(frame_food, text="Chicken w Burger", height=4, width=15, font=('Helvetica', 12), command=lambda: food(2, 1, selected_items, receipt), bg='#ff9999', fg='black')
food8.grid(row=2, column=1, padx=10, pady=10)

food9 = Button(frame_food, text="Spag w Burger", height=4, width=15, font=('Helvetica', 12), command=lambda: food(2, 2, selected_items, receipt), bg='#ff9999', fg='black')
food9.grid(row=2, column=2, padx=10, pady=10)

frame_drinks = Frame(window, bg='white')
frame_drinks.pack(pady=20)

drink1 = Button(frame_drinks, text="Cola", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(0, 0, selected_items, receipt), bg='light blue', fg='black')
drink1.grid(row=0, column=0, padx=10, pady=10)

drink2 = Button(frame_drinks, text="Sprite", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(0, 1, selected_items, receipt), bg='light blue', fg='black')
drink2.grid(row=0, column=1, padx=10, pady=10)

drink3 = Button(frame_drinks, text="Pepsi", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(0, 2, selected_items, receipt), bg='light blue', fg='black')
drink3.grid(row=0, column=2, padx=10, pady=10)

drink4 = Button(frame_drinks, text="Water", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(1, 0, selected_items, receipt), bg='light blue', fg='black')
drink4.grid(row=1, column=0, padx=10, pady=10)

drink5 = Button(frame_drinks, text="Juice", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(1, 1, selected_items, receipt), bg='light blue', fg='black')
drink5.grid(row=1, column=1, padx=10, pady=10)

drink6 = Button(frame_drinks, text="Iced tea", height=4, width=15, font=('Helvetica', 12), command=lambda: drinks(1, 2, selected_items, receipt), bg='light blue', fg='black')
drink6.grid(row=1, column=2, padx=10, pady=10)

total_cost_label = Label(window, text="Total cost: ₱0.00", font=('Helvetica', 16))
total_cost_label.place(relx=1.0, rely=1.0, x=-20, y=-300, anchor=SE)

frame_buttons = Frame(window)
frame_buttons.pack(pady=10)

clear_button = Button(frame_buttons, text="Void All", height=2, width=20, font=('Helvetica', 12), command=lambda: clear_order(selected_items, receipt), bg='#ff9999', fg='black')
clear_button.grid(row=0, column=0, padx=5)

delete_button = Button(frame_buttons, text="Void", height=2, width=20, font=('Helvetica', 12), command=lambda: delete_item(selected_items, receipt), bg='#ff9999', fg='black')
delete_button.grid(row=0, column=1, padx=5)

entry = Entry(frame_buttons, width=5, font=('Helvetica', 16))  # Define the entry widget within frame_buttons
entry.grid(row=0, column=2, padx=5)

payment_entry = Entry(frame_buttons, font=('Helvetica', 16))
payment_entry.grid(row=1, column=0, columnspan=3, pady=5)

# Calculator buttons...
frame_calculator = Frame(window)
frame_calculator.pack(pady=10)
frame_calculator.place(relx=1.0, rely=1.0, x=-20, y=-50, anchor=SE)

equation_text = ""
equation_label = StringVar()
equation_label.set("")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        c_button = Button(frame_calculator, text=button, font=('Helvetica', 12), height=2, width=5, command=clear)
        c_button.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    else:
        Button(frame_calculator, text=button, font=('Helvetica', 12), height=2, width=5, command=lambda num=button: button_press(num)).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Payment buttons
payment_frame = Frame(window)
payment_frame.pack(pady=10)

payment_button = Button(payment_frame, text="Pay", font=('Helvetica', 12), height=2, width=20, command=lambda: pay_and_change(selected_items, payment_entry, change_label, receipt, change_display_receipt, is_discounted_customer), bg='#ff9999', fg='black')
payment_button.grid(row=0, column=0, padx=5)

change_label = Label(payment_frame, text="Change: ₱0.00", font=('Helvetica', 12))
change_label.grid(row=0, column=1, padx=5)

# Discount button
is_discounted_customer = False  # Add this line to track if customer is eligible for discount
discount_button = Button(payment_frame, text="Senior/PWD Discount", font=('Helvetica', 12), height=2, width=20, command=toggle_discount, state=DISABLED, bg='light blue', fg='black')
discount_button.grid(row=0, column=2, padx=5)

# Change display receipt
change_display_receipt = Text(window, font=('Helvetica', 16), bg="white", fg="black", width=21, height=4)
change_display_receipt.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)
change_display_receipt.insert("end", "Change: ₱0.00")
change_display_receipt.config(state=DISABLED)

window.mainloop()

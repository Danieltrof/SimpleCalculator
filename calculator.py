import tkinter as tk

# Function to update the expression in the entry box
def button_click(item):
    current_text = expression.get()
    expression.set(current_text + str(item))

# Function to clear the entry box
def button_clear():
    expression.set("")

# Function to calculate and display the result
def button_equal():
    try:
        current_expression = expression.get()
        # Replace '^' with '**' for Python's exponentiation operator
        current_expression = current_expression.replace('^', '**')
        result = str(eval(current_expression))  # Evaluate the expression
        expression.set(result)
    except Exception as e:
        expression.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to hold the expression
expression = tk.StringVar()

# Create the entry box
entry = tk.Entry(root, textvariable=expression, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Create and place buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '^'
]

row = 1
col = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                  command=button_equal).grid(row=row, column=col)
    elif button == "C":
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                  command=button_clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'),
                  command=lambda b=button: button_click(b)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()

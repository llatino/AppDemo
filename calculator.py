import tkinter as tk

root = tk.Tk()
root.title("Calculatot")

expression = ""

def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def calculate():
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# ช่องแสดงตัวเลข
entry = tk.Entry(root, font=("Arial", 24), justify="right", width=16)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ปุ่มทั้งหมด
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        if label == "=":
            btn = tk.Button(root, text=label, font=("Arial", 18),
                            width=4, height=2, command=calculate)
        else:
            btn = tk.Button(root, text=label, font=("Arial", 18),
                            width=4, height=2, command=lambda v=label: press(v))
        btn.grid(row=r+1, column=c, padx=5, pady=5)

# ปุ่ม Clear
tk.Button(root, text="C", font=("Arial", 18), width=18, height=2,
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
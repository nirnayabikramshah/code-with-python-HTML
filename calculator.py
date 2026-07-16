import tkinter as tk

def press(value):
    entry_box.insert(tk.END, value)

def answer():
    try:
        expression = entry_box.get()
        result = eval(expression)
        
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except Exception:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")

def clear():
    entry_box.delete(0, tk.END)


window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

window.rowconfigure(0, weight=1) 
window.rowconfigure(1, weight=2) 
window.rowconfigure(2, weight=2) 
window.rowconfigure(3, weight=2) 
window.rowconfigure(4, weight=2) 

for col in range(4):
    window.columnconfigure(col, weight=1) 

btn_font = ("Arial", 16, "bold")

entry_box = tk.Entry(window, font=("Arial", 24), justify="right")
entry_box.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10) 

button = tk.Button(window, text="1", font=btn_font, command=lambda: press("1"))
button.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

button2 = tk.Button(window, text="2", font=btn_font, command=lambda: press("2"))
button2.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

button3 = tk.Button(window, text="3", font=btn_font, command=lambda: press("3"))
button3.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

button4 = tk.Button(window, text="4", font=btn_font, command=lambda: press("4"))
button4.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

button5 = tk.Button(window, text="5", font=btn_font, command=lambda: press("5"))
button5.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

button6 = tk.Button(window, text="6", font=btn_font, command=lambda: press("6"))
button6.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

button7 = tk.Button(window, text="7", font=btn_font, command=lambda: press("7"))
button7.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

button8 = tk.Button(window, text="8", font=btn_font, command=lambda: press("8"))
button8.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

button9 = tk.Button(window, text="9", font=btn_font, command=lambda: press("9"))
button9.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

button_minus = tk.Button(window, text="-", font=btn_font, command=lambda: press("-"))
button_minus.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

button_add = tk.Button(window, text="+", font=btn_font, command=lambda: press("+"))
button_add.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

button_multiply = tk.Button(window, text="*", font=btn_font, command=lambda: press("*"))
button_multiply.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

button_clear = tk.Button(window, text="C", font=btn_font, command=clear, fg="red")
button_clear.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

button_backspace = tk.Button(window, text="DEL", font=btn_font, command=lambda: entry_box.delete(len(entry_box.get()) - 1, tk.END), fg="orange")
button_backspace.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)


button_devide = tk.Button(window, text="/", font=btn_font, command=lambda: press("/"))
button_devide.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

button_answer = tk.Button(window, text="=", font=btn_font, command=answer, bg="lightblue")
button_answer.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)

window.mainloop()

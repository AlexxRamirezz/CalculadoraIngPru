import tkinter as tk

def click(event):
    global text_var
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(text_var.get()))
            text_var.set(result)
        except Exception as e:
            text_var.set("Error")
    elif text == "C":
        text_var.set("")
    else:
        text_var.set(text_var.get() + text)

root = tk.Tk()
root.geometry("250x400")
root.title("Calculadora")

text_var = tk.StringVar()
text_var.set("")

entry = tk.Entry(root, textvar=text_var, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '9', '8', '7',
    '6', '5', '4',
    '3', '2', '1',
    '0', '-', '+',
    '/', '*', 'C',
    '='
]

i = 0
for button in buttons:
    b = tk.Button(button_frame, text=button, font="lucida 15 bold", width=5, relief=tk.RAISED, borderwidth=3)
    b.grid(row=i//3, column=i%3, pady=2, padx=2)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()
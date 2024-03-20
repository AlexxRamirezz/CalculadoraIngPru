import tkinter as tk

class CalculadoraConMemoria:
    memoria = 0

    @classmethod
    def sumar_a_memoria(cls, valor):
        cls.memoria += valor

    @classmethod
    def restar_de_memoria(cls, valor):
        cls.memoria -= valor

    @classmethod
    def obtener_memoria(cls):
        return cls.memoria

    @classmethod
    def borrar_memoria(cls):
        cls.memoria = 0 

    @classmethod
    def guardar_en_memoria(cls, valor):
        cls.memoria = valor


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
    elif text.lower() == 'm+':
        try:
            valor = eval(text_var.get())
            CalculadoraConMemoria.sumar_a_memoria(valor)
            text_var.set("")
        except Exception as e:
            text_var.set("Error")
    elif text.lower() == 'm-':
        try:
            valor = eval(text_var.get())
            CalculadoraConMemoria.restar_de_memoria(valor)
            text_var.set("")
        except Exception as e:
            text_var.set("Error")
    elif text.lower() == 'mr':
        text_var.set(str(CalculadoraConMemoria.obtener_memoria()))
    elif text.lower() == 'mc':
        CalculadoraConMemoria.borrar_memoria()
        text_var.set("")
    elif text.lower() == 'ms':
        try:
            valor = eval(text_var.get())
            CalculadoraConMemoria.guardar_en_memoria(valor)
        except Exception as e:
            text_var.set("Error")
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
    '=', 'M+', 'M-',
    'MR', 'MC', 'MS'
]

i = 0
for button in buttons:
    b = tk.Button(button_frame, text=button, font="lucida 15 bold", width=5, relief=tk.RAISED, borderwidth=3)
    b.grid(row=i//4, column=i%4, pady=2, padx=2)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()
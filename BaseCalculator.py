from tkinter import *
from tkinter import ttk
import math
import re
from fractions import Fraction 

def button_click(value):
    current_text = entry1.get()
    if current_text == "0":
        entry1.set(value)
    else:
        entry1.set(current_text + value)

def Button_Erase():
    current_text = entry1.get()
    sequences = {
        "sin": len("sin"),
        "cos": len("cos"),
        "tan": len("tan"),
        "√": len("√")
    }
    for sequence, length in sequences.items():
        if current_text.endswith(sequence):
            NewText = current_text[:-length]
            entry1.set(NewText)
            return
    new_text = current_text[:-1]
    entry1.set(new_text)
        
def Button_Erase_Entry():
    current_text = entry1.get()
    if len(current_text) > 0:
        entry1.set("0")
        
def Erase_All():
    current_text = entry1.get()
    if len(current_text) > 0:
        entry1.set("0")
    current_text2 = entry2.get()
    if len(current_text2) > 0:
        entry2.set(current_text[:0])

    entry2.set(current_text)


def Button_Erase_Entry():
    entry1.set("0")

def Erase_All():
    entry1.set("0")
    entry2.set("")

def subtract(tokens):
    index = 0
    while index < len(tokens):
        token = tokens[index]

        # Si el token es '-', verificamos si es una resta o un número negativo
        if token == '-':
            # Si el '-' está al inicio o precedido por un operador, es un número negativo
            if index == 0 or tokens[index - 1] in ['+', '*', '/', '-']:
                # Combina el '-' con el número siguiente
                tokens[index:index + 2] = [str(float('-' + tokens[index + 1]))]
            else:
                # Es una operación de resta
                result = float(tokens[index - 1]) - float(tokens[index + 1])
                tokens[index - 1] = str(result)
                del tokens[index:index + 2]
        else:
            index += 1

    return tokens



def Calculate(expr):
    expr = expr.replace('x', '*')
    
    # Tokenización de la expresión
    tokens = re.findall(r'[\d\.]+|[+*/-]|\^|cos|:', expr)

    # Procesamiento de fracciones
    while ':' in tokens:
        for index, token in enumerate(tokens):
            if token == ':':
                numerador = float(tokens[index - 1])
                denominador = float(tokens[index + 1])
                resultado = round(numerador / denominador, 3)

                tokens[index - 1] = str(resultado)
                tokens[index] = ''
                tokens[index + 1] = ''
                tokens = list(filter(None, tokens))
                break

    # Procesamiento del coseno
    while 'cos' in tokens:
        for index, token in enumerate(tokens):
            if token == 'cos':
                argumento = float(tokens[index + 1])
                tokens[index:index + 2] = [str(round(math.cos(math.radians(argumento)), 9))]

    # Procesamiento de potenciación
    while '^' in tokens:
        for index in range(len(tokens)):
            if tokens[index] == '^':
                base = float(tokens[index - 1])
                exp = float(tokens[index + 1])
                tokens[index - 1] = str(round(base ** exp, 9))
                del tokens[index:index + 2]
                break

  

   #multiplicaciones
    while '*' in tokens:
        for index in range(len(tokens)):
            if tokens[index] == '*':
                tokens[index - 1] = str(float(tokens[index - 1]) * float(tokens[index + 1]))
                del tokens[index:index + 2]
                break

 # Llamar a la función de resta
    tokens = subtract(tokens)

    # Devuelve el resultado
    return tokens[0] if tokens else "0"


def Equal():
    current_text = entry1.get().strip()
    
    try:
        resultado = Calculate(current_text)
    except Exception as e:
        resultado = "Error"

    entry2.set(resultado)

def Press_Key(event):
    key = event.char
    if key.isdigit():
        button_click(key)
    elif key in ['+', '-', 'x', '÷']:
        button_click(key.replace('x', '*').replace('÷', '/'))  # Cambiar x y ÷ a * y /
    elif key == '.':
        button_click('.')
    elif key == '\r':
        Equal()
    elif key == '\b':
        Button_Erase()

def Button_Craft(parent, text, command, row, col, rowspan=1, colspan=1, bg="#131313", fg="white"):
    button = Button(parent, text=text, borderwidth=0, highlightthickness=0, relief="flat", 
                    command=command, padx=10, pady=10, width=6, height=1, font=('Segoe UI', 20), bg=bg, fg=fg)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")
    
    # Evento para cambiar el color al pasar el cursor sobre el botón
    button.bind("<Enter>", lambda e: button.config(bg="#2a2828"))
    
    # Evento para restaurar el color original cuando el cursor sale del botón
    button.bind("<Leave>", lambda e: button.config(bg=bg))
    
    return button

root = Tk()
root.configure(bg="#f7f4f4")
root.title("Calculadora")
root.geometry("+800+200")

mainframe = Frame(root, bg="#111111")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

for i in range(4):
    mainframe.columnconfigure(i, weight=1)
for i in range(9):
    mainframe.rowconfigure(i, weight=1)

entry1 = StringVar(value="0")
entry2 = StringVar()

label_entry1 = Label(mainframe, textvariable=entry1, anchor='e', font=("Verdana", 24), bg="#000000", fg="#ffffff")
label_entry1.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))

label_entry2 = Label(mainframe, textvariable=entry2, anchor='e', font=("Verdana", 32), bg="#000000", fg="#ffffff")
label_entry2.grid(column=0, row=1, columnspan=4, sticky=(N, S, E, W))

Button_Craft(mainframe, "√", lambda: button_click("√"), 2, 0)
Button_Craft(mainframe, "CE", Button_Erase_Entry, 2, 1)
Button_Craft(mainframe, "C", Erase_All, 2, 2)
Button_Craft(mainframe, "←", Button_Erase, 2, 3)

dropdown_button = Menubutton(mainframe, text="Trig.", relief="flat", font=('Segoe UI', 18), bg="#131313", fg="#ffffff")
dropdown_button.grid(row=3, column=0, sticky="nsew")

dropdown_menu = Menu(dropdown_button, tearoff=0)
dropdown_menu.config(bg="#131313", fg="#ffffff")  
dropdown_button.config(menu=dropdown_menu)

dropdown_menu.add_command(label="Seno", command=lambda: button_click("sin"), font=('Segoe UI', 20))
dropdown_menu.add_command(label="Coseno", command=lambda: button_click("cos"), font=('Segoe UI', 20))
dropdown_menu.add_command(label="Tangente", command=lambda: button_click("tan"), font=('Segoe UI', 20))

dropdown_button.bind("<Enter>", lambda e: dropdown_button.config(bg="#525050"))
dropdown_button.bind("<Leave>", lambda e: dropdown_button.config(bg="#131313"))

dropdown_button["menu"] = dropdown_menu

Button_Craft(mainframe, "x²", lambda: button_click("^"), 3, 1)
Button_Craft(mainframe, ":", lambda: button_click(":"), 3, 2)
Button_Craft(mainframe, "÷", lambda: button_click("÷"), 3,3) 

Button_Craft(mainframe, "7", lambda: button_click("7"), 4, 0)
Button_Craft(mainframe, "8", lambda: button_click("8"), 4, 1)
Button_Craft(mainframe, "9", lambda: button_click("9"), 4, 2)
Button_Craft(mainframe, "x", lambda: button_click("x"), 4, 3)

Button_Craft(mainframe, "4", lambda: button_click("4"), 5, 0)
Button_Craft(mainframe, "5", lambda: button_click("5"), 5, 1)
Button_Craft(mainframe, "6", lambda: button_click("6"), 5, 2)
Button_Craft(mainframe, "−", lambda: button_click("-"), 5, 3)

Button_Craft(mainframe, "1", lambda: button_click("1"), 6, 0)
Button_Craft(mainframe, "2", lambda: button_click("2"), 6, 1)
Button_Craft(mainframe, "3", lambda: button_click("3"), 6, 2)
Button_Craft(mainframe, "+", lambda: button_click("+"), 6, 3)

Button_Craft(mainframe, "%", lambda: button_click("%"), 7, 0)
Button_Craft(mainframe, "0", lambda: button_click("0"), 7, 1)
Button_Craft(mainframe, ".", lambda: button_click("."), 7, 2)
Button_Craft(mainframe, "=", Equal, 7, 3)


root.bind("<Key>", Press_Key)

root.mainloop()
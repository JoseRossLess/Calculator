
from tkinter import *
from tkinter import ttk
import math
import re

DoneOp = False
def button_click(value):
    global DoneOp
    # Si se ha realizado una operación, borra entry1 antes de agregar un nuevo valor
    if DoneOp:
        entry1.set(value)  # Empieza de nuevo con el nuevo número
        DoneOp = False  # Reinicia la variable
    else:
        # Solo añade el valor al entry1
        if entry1.get() == "0":
            entry1.set(value)
        else:
            entry1.set(entry1.get() + value)
            
def Button_Erase():
    current_text = entry1.get()
    sequences = {
        "Ans": len("Ans"),
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

Last_Result = None

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


        if token == '+':
            if index == 0 or tokens[index - 1] in ['+', '-', '*', '/']:
                tokens[index:index + 2] = [str(float(tokens[index + 1]))] 
            else:
                result = float(tokens[index - 1]) + float(tokens[index + 1])
                tokens[index - 1] = str(result)
                del tokens[index:index + 2]
        else:
            index += 1
    return tokens

def Calculate(expr):

    global Last_Result
    
    if "Ans" in expr:
        expr = expr.replace("Ans", str(Last_Result) if Last_Result is not None else "0")
    
    expr = expr.replace('x', '*')
    expr = expr.replace('÷', '/')

    expr = expr.replace('÷', '/')
    Tokens = re.findall(r'[\d\.]+|[+*/-]|\^|cos|√|:', expr) 

    # fraccion Edin 
    while ':' in Tokens: # Si encuentra :
        for index, funcion in enumerate (Tokens): # para recorrer la lista de tokens usando enumarete
            if funcion in (':'):
                numerador = float(Tokens[index - 1])
                denominador = float(Tokens[index + 1])
                resultado = round(numerador / denominador, 3)

                Tokens[index - 1] = str(resultado)
                Tokens[index] = ''
                Tokens[index + 1] = ''
                Tokens = list(filter(None, Tokens))
                break

    # coseno daniel 
    while 'cos' in Tokens:  # Ejecutar el bucle mientras haya un token llamado 'cos' en la lista Tokens
        for index, token in enumerate(Tokens):
            if token == 'cos':  # busca la función coseno 
                siguiente_token = Tokens[index + 1]
                if siguiente_token == '-' and index + 2 < len(Tokens):  # Si es un número negativo salata al siguente token
                    argumento = float(Tokens[index + 1] + Tokens[index + 2])  # combina el signo y el número
                    Tokens[index:index + 3] = [str(round(math.cos(math.radians(argumento)), 9))]  # Calculamos el coseno con el signo negativo
                else:  # Si no es negativo
                    argumento = float(siguiente_token)  # opera normalmente
                    Tokens[index:index + 2] = [str(round(math.cos(math.radians(argumento)), 9))]  # Calculamos el coseno


    # potenciacion Osvaldo

    while '^' in Tokens:
        for index in range(len(Tokens)):
            if Tokens[index] == '^':
                base = float(Tokens[index - 1]) if Tokens[index - 1] != '-' else -float(Tokens[index - 2])
                exp = float(Tokens[index + 1]) if Tokens[index + 1] != '-' else -float(Tokens[index + 2])
                Tokens[index - 1] = str(round(base ** exp, 9))
                del Tokens[index:index + 2]
                break 

    #Raiz Luisa
    while '√' in Tokens: # Nombra a la funcion que corresponde en el listado 
        for idx, elemento in enumerate(Tokens): 
            if elemento == '√': #Busca la funcion
                siguiente_elemento = Tokens[idx + 1] 
                razon = float(siguiente_elemento)
                Tokens[idx:idx + 2] = [str(round(math.sqrt(razon), 9))] #Formula para realizar la raiz


    # Llamar a la función de operaciones generales


    # Llamar a la función de


    ##Usar numeros posteriores como argumentos en fucniones trigonometricas y radicación

    #45+8-8*5
    def Operation(LisTokens):

        

#Jeremias Division Combinada Con Multiplicacion 

        while '*' in LisTokens or '/' in LisTokens:
            for i in range(len(LisTokens)):
                if LisTokens[i] == '*':
                    LisTokens[i - 1] = str(float(LisTokens[i - 1]) * float(LisTokens[i + 1]))
                    del LisTokens[i:i + 2]
                    break
                elif LisTokens[i] == '/':
                        LisTokens[i - 1] = str(float(LisTokens[i - 1]) / float(LisTokens[i + 1]))
                        del LisTokens[i:i + 2]
                        break

                


        LisTokens = subtract(LisTokens)



        ##Operar sumas, restas, multiplicación, etc. 

        return LisTokens[0] if LisTokens else "0"

    return Operation(Tokens)

def Equal():
    global Last_Result, Display_Result, DoneOp
    
    current_text = entry1.get().strip()
    
    try:
        Result = Calculate(current_text)
        Last_Result = float(Result)
        DoneOp = True
        Display_Result = True  # Marca que el último resultado está disponible
    except Exception as e:
        Result = "Syntax Error"
        Last_Result = None
        Display_Result = False

    entry2.set(Result)


def Press_Key(event):
    key = event.char
    if key.isdigit():
        button_click(key)
    elif key in ['+', '-', '*', '/']:
        button_click(key.replace('*', 'x').replace('/', '÷'))  # Cambiar x y ÷ a * y /
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

button_state = "CE"  # Corrige el nombre de la variable

def Erase_Entrys():
    global button_state
    if button_state == 'CE':
        entry1.set("0")  # Borra solo entry1
        button_state = "C"  # Actualiza el estado
        Button_EraseEntry.config(text='C')  # Cambia el texto a 'C'
    else:
        entry1.set("0")  # Borra entry1
        entry2.set("")    # Borra entry2
        button_state = "CE"  # Actualiza el estado
        Button_EraseEntry.config(text='CE')  # Cambia el texto a 'CE'
        
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
Button_Craft(mainframe, "Ans", lambda: button_click ("Ans"), 2, 1)
Button_EraseEntry = Button_Craft(mainframe, "CE", Erase_Entrys, 2, 2)
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
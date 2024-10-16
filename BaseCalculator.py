
# Para la parte visual de la calculadora se escibe el siguiente codigo 
# Se implementa la extensión Tkinter Snnipets que es una biblioteca gráfica para Python
from tkinter import *
from tkinter import ttk
import math

def button_click(value):
    current_text = entry1.get()
    # Si el texto actual es "0", reemplázalo con el nuevo valor
    if current_text == "0":
        entry1.set(value)
    else:
        entry1.set(current_text + value)
        
def Button_Erase():
    current_text = entry1.get()
    sequences = {
        "sin": len("sin"),
        "cos": len("cos"),
        "tan": len("tan")
    }
    for sequence, length in sequences.items():
        if current_text.endswith(sequence):
            new_text = current_text[:-length]
            entry1.set(new_text)
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
        
def Equal():
    current_text = entry1.get()
    entry2.set(current_text)

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número."""
    if numero < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(numero)

def menu():
    """Muestra el menú de opciones."""
    print("Seleccione una opción:")
    print("1. Calcular la raíz cuadrada")
    print("2. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            numero = float(input("Ingrese un número: "))
            resultado = raiz_cuadrada(numero)
            print(f"La raíz cuadrada de {numero} es: {resultado}")
        elif opcion == '2':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if 'name'== "main":
    main()

root = Tk()
root.title("Calculadora")

root.geometry("+800+80") #con esto establecemos dónde aparecera la ventana de la aplicación

style = ttk.Style()
style.configure("Custom.TButton", font = ("Arial",18))

styles = ttk.Style()
styles.configure('mainframe.TFrame', background ="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky = (N, S, E, W))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

for i in range(4):
    mainframe.columnconfigure(i, weight = 1)
for i in range (9):
    mainframe.rowconfigure(i, weight = 1)

entry1 = StringVar()
entry1.set("0")
label_entry1 = ttk.Label(mainframe, textvariable = entry1, anchor='e', font=("Arial", 24))
label_entry1.grid(column=0, row=0, columnspan= 4, sticky= (N, S, W, E))

entry2 = StringVar()
entry2.set("")
label_entry2 = ttk.Label(mainframe, textvariable = entry2, anchor='e', font=("Arial", 25))
label_entry2.grid(column=0, row=1, columnspan= 4, sticky= (N, S, W, E))

#region Botones de borrado y Operaciones
#Se empieza a crear cada uno de los botones para la calculdora
buttonClear_Entry = ttk.Button(mainframe, text = "CE", command = Button_Erase_Entry, style = "Custom.TButton")
buttonClear_All = ttk.Button(mainframe, text = "C", command = Erase_All, style = "Custom.TButton")
buttonErase = ttk.Button(mainframe, text = "←", command = Button_Erase, style = "Custom.TButton")
buttonEqual = ttk.Button(mainframe, text = "=", command = Equal, style = "Custom.TButton")

division_button = ttk.Button(mainframe, text = "÷", command=lambda: button_click("÷"), style = "Custom.TButton")
multiplication_button = ttk.Button(mainframe, text = "x", command=lambda: button_click("x"), style = "Custom.TButton")
add_button = ttk.Button(mainframe, text = "+", command=lambda: button_click("+"), style = "Custom.TButton")
subtract_button = ttk.Button(mainframe, text = "-", command=lambda: button_click("-"), style = "Custom.TButton")
squareroot_button = ttk.Button(mainframe, text = "√", command=lambda: button_click("√"), style = "Custom.TButton")
expon_button = ttk.Button(mainframe, text = "x²", command=lambda: button_click("x²"), style = "Custom.TButton")
fraction_button = ttk.Button(mainframe, text = "a⅓", command=lambda: button_click("/"), style = "Custom.TButton")

sin_button = ttk.Button(mainframe, text = "sin", command=lambda: button_click("sin"), style = "Custom.TButton")
cos_button = ttk.Button(mainframe, text = "cos", command=lambda: button_click("cos"), style = "Custom.TButton")
tan_button = ttk.Button(mainframe, text = "tan", command=lambda: button_click("tan"), style = "Custom.TButton")

point_button = ttk.Button(mainframe, text = ".", command=lambda: button_click("."), style = "Custom.TButton")
percentage_button = ttk.Button(mainframe, text ="%", command=lambda: button_click("%"), style = "Custom.TButton")

#endregion

#region Botones Númericos
button_0= ttk.Button(mainframe, text = "0", command=lambda: button_click("0"), style = "Custom.TButton")
button_1= ttk.Button(mainframe, text = "1", command=lambda: button_click("1"), style = "Custom.TButton")
button_2= ttk.Button(mainframe, text = "2", command=lambda: button_click("2"), style = "Custom.TButton")
button_3= ttk.Button(mainframe, text = "3", command=lambda: button_click("3"), style = "Custom.TButton")
button_4= ttk.Button(mainframe, text = "4", command=lambda: button_click("4"), style = "Custom.TButton")
button_5= ttk.Button(mainframe, text = "5", command=lambda: button_click("5"), style = "Custom.TButton")
button_6= ttk.Button(mainframe, text = "6", command=lambda: button_click("6"), style = "Custom.TButton")
button_7= ttk.Button(mainframe, text = "7", command=lambda: button_click("7"), style = "Custom.TButton")
button_8= ttk.Button(mainframe, text = "8", command=lambda: button_click("8"), style = "Custom.TButton")
button_9= ttk.Button(mainframe, text = "9", command=lambda: button_click("9"), style = "Custom.TButton")
#endregion

#region Ubicacion de Botones y Ajuste al Mainframe
#aquí ordenamos los botones dentro del Frame
#Primera fila de botones
fraction_button.grid(column = 0, row = 2,sticky = (N, S, E, W))
buttonClear_All.grid(column = 1, row = 2, sticky = (N, S, E, W))
buttonClear_Entry.grid(column = 2, row = 2, sticky = (N, S, E, W))
buttonErase.grid(column = 3, row = 2, sticky = (N, S, E, W))

#segunda fila de botones
sin_button.grid(column = 0, row = 3, sticky = (N, S, E, W))
cos_button.grid(column = 1, row =3, sticky = (N, S, E, W))
tan_button.grid(column = 2, row =3, sticky = (N, S, E, W))
division_button.grid(column = 3, row =3, sticky = (N, S, E, W))

#tercera fila de botones
button_7.grid(column = 0, row = 4, sticky = (N, S, E, W))
button_8.grid(column = 1, row = 4, sticky = (N, S, E, W))
button_9.grid(column = 2, row = 4, sticky = (N, S, E, W))
multiplication_button.grid(column = 3, row = 4, sticky = (N, S, E, W))

#cuarta fila de botones
button_4.grid(column = 0, row = 5, sticky = (N, S, E, W))
button_5.grid(column = 1, row = 5, sticky = (N, S, E, W))
button_6.grid(column = 2, row = 5, sticky = (N, S, E, W))
subtract_button.grid(column = 3, row = 5, sticky = (N, S, E, W))

#quinta fial de botones
button_1.grid(column = 0, row = 6, sticky = (N, S, E, W))
button_2.grid(column = 1, row = 6, sticky = (N, S, E, W))
button_3.grid(column = 2, row = 6, sticky = (N, S, E, W))
add_button.grid(column = 3, row = 6, sticky = (N, S, E, W))

#sexta fila
percentage_button.grid(column = 0, row = 7, sticky = (N, S, E, W))
button_0.grid(column = 1, row = 7, sticky = (N, S, E, W))
point_button.grid(column = 2, row = 7, sticky = (N, S, E, W))
buttonEqual.grid(column = 3, row = 7, sticky = (N, S, E, W))


#fila extra
expon_button.grid(column = 0, row = 8, sticky = (N, S, E, W))
squareroot_button.grid(column = 1, row = 8, sticky = (N, S, E, W))

#endregion

root, mainloop() 
#NameChange

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
    
root = Tk()
root.title("Calculadora")

root.geometry("+800+80") #con esto establecemos dónde aparecera la ventana de la aplicación

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
label_entry2 = ttk.Label(mainframe, textvariable = entry2)
label_entry2.grid(column=0, row=1, columnspan= 4, sticky= (N, S, W, E))

#Se empieza a crear cada uno de los botones para la calculdora
buttonClear_Entry = ttk.Button(mainframe, text = "CE")
buttonClear_All = ttk.Button(mainframe, text = "C")
buttonErase = ttk.Button(mainframe, text = "←")
buttonEqual = ttk.Button(mainframe, text = "=")

division_button = ttk.Button(mainframe, text = "÷")
multiplication_button = ttk.Button(mainframe, text = "x")
add_button = ttk.Button(mainframe, text = "+")
subtract_button = ttk.Button(mainframe, text = "-")
squareroot_button = ttk.Button(mainframe, text = "√")
expon_button = ttk.Button(mainframe, text = "x²")
fraction_button = ttk.Button(mainframe, text = "a⅓")

sin_button = ttk.Button(mainframe, text = "sin")
cos_button = ttk.Button(mainframe, text = "cos")
tan_button = ttk.Button(mainframe, text = "tan")

point_button = ttk.Button(mainframe, text = ".")
percentage_button = ttk.Button(mainframe, text ="%")

button_0= ttk.Button(mainframe, text = "0", command=lambda: button_click("0"))
button_1= ttk.Button(mainframe, text = "1", command=lambda: button_click("1"))
button_2= ttk.Button(mainframe, text = "2", command=lambda: button_click("2"))
button_3= ttk.Button(mainframe, text = "3", command=lambda: button_click("3"))
button_4= ttk.Button(mainframe, text = "4", command=lambda: button_click("4"))
button_5= ttk.Button(mainframe, text = "5", command=lambda: button_click("5"))
button_6= ttk.Button(mainframe, text = "6", command=lambda: button_click("6"))
button_7= ttk.Button(mainframe, text = "7", command=lambda: button_click("7"))
button_8= ttk.Button(mainframe, text = "8", command=lambda: button_click("8"))
button_9= ttk.Button(mainframe, text = "9", command=lambda: button_click("9"))

#aquí ordenamos los botones dentro del Frame
#Primera fila de botones
fraction_button.grid(column = 0, row = 2, sticky = (N, S, E, W))
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

root, mainloop()
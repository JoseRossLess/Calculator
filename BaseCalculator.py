
# Para la parte visual de la calculadora se escibe el siguiente codigo 
# Se implementa la extensión Tkinter Snnipets que es una biblioteca gráfica para Python
from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")

root.geometry("+800+80") #con esto establecemos dónde aparecera la ventana de la aplicación

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

entry1 = StringVar()
label_entry1 = ttk.Label(mainframe, textvariable = entry1)
label_entry1.grid(column=0, row=0)

entry2 = StringVar()
label_entry2 = ttk.Label(mainframe, textvariable = entry2)
label_entry2.grid(column=0, row=1)

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

button_0= ttk.Button(mainframe, text = "0")
button_1= ttk.Button(mainframe, text = "1")
button_2= ttk.Button(mainframe, text = "2")
button_3= ttk.Button(mainframe, text = "3")
button_4= ttk.Button(mainframe, text = "4")
button_5= ttk.Button(mainframe, text = "5")
button_6= ttk.Button(mainframe, text = "6")
button_7= ttk.Button(mainframe, text = "7")
button_8= ttk.Button(mainframe, text = "8")
button_9= ttk.Button(mainframe, text = "9")

#aquí ordenamos los botones dentro del Frame
#Primera fila de botones
fraction_button.grid(column = 0, row = 2)
buttonClear_All.grid(column = 1, row = 2)
buttonClear_Entry.grid(column = 2, row = 2)
buttonErase.grid(column = 3, row = 2)

#segunda fila de botones
sin_button.grid(column = 0, row = 3)
cos_button.grid(column = 1, row =3)
tan_button.grid(column = 2, row =3)
division_button.grid(column = 3, row =3)

#tercera fila de botones
button_7.grid(column = 0, row = 4)
button_8.grid(column = 1, row = 4)
button_9.grid(column = 2, row = 4)
multiplication_button.grid(column = 3, row = 4)

#cuarta fila de botones
button_4.grid(column = 0, row = 5)
button_5.grid(column = 1, row = 5)
button_6.grid(column = 2, row = 5)
subtract_button.grid(column = 3, row = 5)

#quinta fial de botones
button_1.grid(column = 0, row = 6)
button_2.grid(column = 1, row = 6)
button_3.grid(column = 2, row = 6)
add_button.grid(column = 3, row = 6)

#sexta fila
percentage_button.grid(column = 0, row = 7)
button_0.grid(column = 1, row = 7)
point_button.grid(column = 2, row = 7)
buttonEqual.grid(column = 3, row = 7)

#fila extra
expon_button.grid(column = 0, row = 8)
squareroot_button.grid(column = 1, row = 8)
root, mainloop()
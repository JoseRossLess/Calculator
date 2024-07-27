
# Para la parte visual de la calculadora se escibe el siguiente codigo 
# Se implementa la extensión Tkinter Snnipets que es una biblioteca gráfica para Python
from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")

root.geometry("+800+80") #con esto establecemos dónde aparecera la ventana de la aplicación

mainframe = ttk.frame(root)
mainframe.gridd(column=0, row=0)

entry1 = StringVar()
label_entry1 = ttk.label(mainframe, textvarible = entry1)
label_entry1.grid(column=0, row=0)

entry2 = StringVar()
label_entry2 = ttk.label(mainframe, textvarible = entry2)

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



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

def Press_Key (event):
    key = event.char
    if key.isdigit():
        button_click(key)
    elif key in ['+','-','*','/']:
        button_click(key)
    elif key == '.':
        button_click('.')
    elif key == '\r':
        Equal()
    elif key == '\b':
        Button_Erase()

def Button_Craft(parent, text, command, row, col, rowspan = 1, colspan = 1, bg = "#f0f0f0", fg = "black"):
    button = Button(parent, text = text, command = command, padx = 20, pady =20, font = ('Arial', 18),  bg = bg, fg = fg,)
    button.grid(row = row, column = col, rowspan = rowspan, columnspan = colspan, sticky = "nsew")
    return button

root = Tk()
root.title("Calculadora")
root.geometry("+800+80") #con esto establecemos dónde aparecera la ventana de la aplicación

mainframe = Frame(root, bg = "#DBDBDB")
mainframe.grid(column = 0, row = 0, sticky = (N, S, E, W))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

for i in range(4):
    mainframe.columnconfigure(i, weight = 1)
for i in range(9):
    mainframe.rowconfigure(i, weight = 1)
    
entry1 = StringVar(value = "0")
entry2 = StringVar

label_entry1 = Label(mainframe, textvariable = entry1, anchor = 'e', font = ("Arial", 24), bg = "#FFFFFF", fg = "#000000" )
label_entry1.grid(column = 0, row = 0, columnspan = 4, sticky = (N, S, E, W))

label_entry2 = Label(mainframe, textvariable = entry2, anchor = 'e', font = ("Arial", 26), bg = "#FFFFFF", fg = "#000000" )
label_entry2.grid(column = 0, row = 1, columnspan = 4, sticky = (N, S, E, W))

root.bind('<Key>',Press_Key)

root.mainloop() 
#NameChange
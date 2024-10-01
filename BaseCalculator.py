from tkinter import *
from tkinter import ttk
import math

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
    entry1.set("0")

def Erase_All():
    entry1.set("0")
    entry2.set("")

def Equal():
    current_text = entry1.get()
    entry2.set(current_text)

def Press_Key(event):
    key = event.char
    if key.isdigit():
        button_click(key)
    elif key in ['+', '-', '*', '/']:
        button_click(key)
    elif key == '.':
        button_click('.')
    elif key == '\r':
        Equal()
    elif key == '\b':
        Button_Erase()

def Button_Craft(parent, text, command, row, col, rowspan=1, colspan=1, bg="#f0f0f0", fg="black"):
    button = Button(parent, text=text, command=command, padx=20, pady=20, font=('Arial', 18), bg=bg, fg=fg)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew")
    return button

root = Tk()
root.title("Calculadora")
root.geometry("+800+100")

mainframe = Frame(root, bg="#DBDBDB")
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

for i in range(4):
    mainframe.columnconfigure(i, weight=1)
for i in range(9):
    mainframe.rowconfigure(i, weight=1)

entry1 = StringVar(value="0")
entry2 = StringVar()

label_entry1 = Label(mainframe, textvariable=entry1, anchor='e', font=("Arial", 24), bg="#FFFFFF", fg="#000000")
label_entry1.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))

label_entry2 = Label(mainframe, textvariable=entry2, anchor='e', font=("Arial", 26), bg="#FFFFFF", fg="#000000")
label_entry2.grid(column=0, row=1, columnspan=4, sticky=(N, S, E, W))

Button_Craft(mainframe, "√", lambda: button_click("√"), 2, 0, bg="#FFD700")
Button_Craft(mainframe, "CE", Button_Erase_Entry, 2, 1)
Button_Craft(mainframe, "C", Erase_All, 2, 2)
Button_Craft(mainframe, "←", Button_Erase, 2, 3)

# Crear Menubutton para funciones trigonométricas
dropdown_button = Menubutton(mainframe, text="Trig.", relief=RAISED, font=('Arial', 18))
dropdown_button.grid(row=3, column=0, sticky="nsew")   # Cambia la posición según sea necesario
dropdown_menu = Menu(dropdown_button, tearoff=0)
dropdown_button.config(menu=dropdown_menu)
dropdown_menu.add_command(label="Seno", command=lambda: button_click("sin"))
dropdown_menu.add_command(label="Coseno", command=lambda: button_click("cos"))
dropdown_menu.add_command(label="Tangente", command=lambda: button_click("tan"))

Button_Craft(mainframe, "x²", lambda: button_click("x²"), 3, 1)
Button_Craft(mainframe, "a⅓", lambda: button_click("a⅓"), 3, 2)
Button_Craft(mainframe, "÷", lambda: button_click("÷"), 3, 3)

Button_Craft(mainframe, "7", lambda: button_click("7"), 4, 0)
Button_Craft(mainframe, "8", lambda: button_click("8"), 4, 1)
Button_Craft(mainframe, "9", lambda: button_click("9"), 4, 2)
Button_Craft(mainframe, "x", lambda: button_click("x"), 4, 3)

Button_Craft(mainframe, "4", lambda: button_click("4"), 5, 0)
Button_Craft(mainframe, "5", lambda: button_click("5"), 5, 1)
Button_Craft(mainframe, "6", lambda: button_click("6"), 5, 2)
Button_Craft(mainframe, "-", lambda: button_click("-"), 5, 3)

Button_Craft(mainframe, "1", lambda: button_click("1"), 6, 0)
Button_Craft(mainframe, "2", lambda: button_click("2"), 6, 1)
Button_Craft(mainframe, "3", lambda: button_click("3"), 6, 2)
Button_Craft(mainframe, "+", lambda: button_click("+"), 6, 3)

Button_Craft(mainframe, "%", lambda: button_click("%"), 7, 0)
Button_Craft(mainframe, "0", lambda: button_click("0"), 7, 1)
Button_Craft(mainframe, ".", lambda: button_click("."), 7, 2)
Button_Craft(mainframe, "=", Equal, 7, 3)

root.bind('<Key>', Press_Key)

root.mainloop()
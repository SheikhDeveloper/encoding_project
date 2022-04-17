
from tkinter import ttk
import tkinter
import string
from actions import *

cyr_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def make_button(frame: ttk.Frame, label: ttk.Label, text: str) -> ttk.Button:
    # Buttons for chars
    button = ttk.Button(frame, text=text, command=button_action(text, label))
    return button


def button_layout(frame: ttk.Frame, label: ttk.Label):
    # Lays out the char buttons, returns the last used row
    latin_alphabet = string.ascii_lowercase

    for i in range(len(latin_alphabet)):
        make_button(frame, label, latin_alphabet[i]).grid(row=2 + i//10, column=i%10)
        last_row_ascii = 2 + i//10

    for i in range(len(cyr_alphabet)):
        make_button(frame, label, cyr_alphabet[i]).grid(row=last_row_ascii + 1 + i//10, column=i%10)
        last_row_cyr = last_row_ascii + 1 + i//10

    for i in range(len(string.punctuation)):
        make_button(frame, label, string.punctuation[i]).grid(row=last_row_cyr + 1 + i//10, column=i%10)
        last_row_punct = last_row_cyr + 1 + i//10

    for i in range(10):
        make_button(frame, label, str(i)).grid(row=last_row_punct + 1 + i//10, column=i%10)
    
    return last_row_punct + 1 + i//10


def make_entry(frame: ttk.Frame, label: ttk.Label, row: int):
    entry = ttk.Entry(frame)
    button = ttk.Button(frame, text="Search!", command=entry_action(entry, label))
    entry.grid(row=row, column=10)
    button.grid(row=row, column=11)


def make_app():
    app = tkinter.Tk()
    frame = ttk.Frame(app)
    frame.grid(column=0, row=0, sticky=("N","E","W","S"))

    label = ttk.Label(frame, text="smth")
    label.grid(row=1,column=1)

    last_row = button_layout(frame, label)

    make_entry(frame, label, last_row + 1)
    
    return app
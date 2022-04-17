import requests
from tkinter.ttk import Label, Entry

url = "http://127.0.0.1:5000/"

def button_action(text: str, label: Label):
    # A callback action for the char buttons
    def change_label():
        response = requests.get(url + "codes/" + text)
        if response.status_code == 404:
            return
        else:
            label["text"] = response.json()

    return change_label


def entry_action(entry: Entry, label: Label):
    def change_label():
        text = entry.get()
        response = requests.get(url + "chars/" + text)
        if response.status_code == 404:
            label["text"] = "Invalid input"
        else:
            label["text"] = response.json()

    return change_label
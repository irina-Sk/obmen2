import requests
import json
from tkinter import*
from tkinter import messagebox as mb

window = Tk()
window.title("Курс обмена валют")
window.geometry("400x200")

Label(text="введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="курс обмена к доллару", command=exchenge).pack(padx=10, pady=10)

window.mainloop()












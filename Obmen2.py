from http.client import responses

import requests
import json
from tkinter import*
from tkinter import messagebox as mb


def exchange():
    code = entry.get()
    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data['rates']
                exchange_rate = ['rates'][code]
                mb.showinfo("курс обмена", f"Курс {exchange_rate}-{code} за доллар")
            else:
                mb.showerror("Ошибка", f"валюта {code} не найдена")

        except Exceotion as e:
            mb.showerror("Ошибка", f"ошибка {e}")
    else:
        mb.showwarning("Внимание!"б f"Введите код валюты")


window = Tk()
window.title("Курс обмена валют")
window.geometry("400x200")

Label(text="введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="курс обмена к доллару", command=exchenge).pack(padx=10, pady=10)

window.mainloop()












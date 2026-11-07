from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests



# Словарь: id  - название
cryptocurrencies = {
    'bitcoin': 'Биткоин',
    'ethereum': 'Эфириум',
    'binancecoin': 'BNB',
    'solana': 'Solana',
    'ripple': 'XRP',
    'cardano': 'Cardano',
    'dogecoin': 'Dogecoin',
    'litecoin': 'Litecoin',
    'tron': 'TRON'
}


root = Tk()
root.title('Курс криптовалюты к USD')
root.geometry('350x150')


root.mainloop()
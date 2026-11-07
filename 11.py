from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_crypto_label(event):
    code = crypto_combobox.get()
    name = cryptocurrencies[code]
    crypto_label.config(text=name)


def get_crypto_price():
    crypto_id = crypto_combobox.get().strip()

    if crypto_id:
        try:
            # Запрашиваем цену выбранной криптовалюты к доллару США
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Ответ например биткоин {"bitcoin": {"usd": 75933}}

            price = data[crypto_id]["usd"]
            name = cryptocurrencies[crypto_id]

            mb.showinfo(
                'Курс криптовалюты',
            #    f'1 {crypto_id} ({name}) = {price:,.2f} USD'
                f'1 {crypto_id} ({name}) = {price:,.2f} USD'
            )

        except Exception as er:
            mb.showerror('Ошибка', str(er))
    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту')


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


Label(root, text='Криптовалюта', font=('Arial', 10, 'bold')).pack(pady=(10, 2))
crypto_combobox = ttk.Combobox(root, values=list(cryptocurrencies.keys()))
crypto_combobox.set('bitcoin')  # Значение по умолчанию
crypto_combobox.pack(pady=3, padx=10)
crypto_combobox.bind('<<ComboboxSelected>>', update_crypto_label)
crypto_label = ttk.Label(text=cryptocurrencies['bitcoin'])
crypto_label.pack()

Button(text='Получить курс', command=get_crypto_price).pack(pady=25)

root.mainloop()

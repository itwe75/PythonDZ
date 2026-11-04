from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_base1_label(event):
    code = base1_combobox.get()
    name = currencies[code]
    base1_label.config(text=name)


def update_base2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)


def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def exchange():
    base1_code = base1_combobox.get().strip()
    base2_code = base2_combobox.get().strip()
    target_code = target_combobox.get().strip()

    if base1_code and base2_code and target_code:
        try:
            # Запрашиваем данные
            response = requests.get(f'https://open.er-api.com/v6/latest/{target_code}')
            response.raise_for_status()
            data = response.json()

            if base1_code in data['rates'] and base2_code in data['rates']:
                # Вычисляем, сколько целевой валюты дают за 1 единицу базовой
                # (т.к. API отдает стоимость 1 целевой валюты в базовых)
                rate1 = 1 / data['rates'][base1_code]
                rate2 = 1 / data['rates'][base2_code]

                target_name = currencies[target_code]

                # Формируем текст результата
                result_text = (
                    f"1 {base1_code} = {rate1:.4f} {target_code} ({target_name})\n"
                    f"1 {base2_code} = {rate2:.4f} {target_code} ({target_name})"
                )
                mb.showinfo('Курс обмена',
                             f'Курс: {rate1:.1f} {target_name} за 1 {currencies[base1_code]}\n'
                             f'Курс: {rate2:.1f} {target_name} за 1 {currencies[base2_code]}')

            else:
                mb.showerror('Ошибка', 'Одна из выбранных валют не найдена в базе API')
        except Exception as er:
            mb.showerror('Ошибка', str(er))
    else:
        mb.showwarning('Внимание', 'Выберите все валюты')


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курсы обмена валют')
root.geometry('380x480')

# Первая базовая валюта
Label(root, text='Базовая валюта', font=('Arial', 10, 'bold')).pack(pady=(10, 2))
base1_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base1_combobox.set('EUR')  # Значение по умолчанию
base1_combobox.pack(pady=3, padx=10)
base1_combobox.bind('<<ComboboxSelected>>', update_base1_label)
base1_label = ttk.Label(text=currencies['EUR'])
base1_label.pack()

# Вторая базовая валюта
Label(root, text='Вторая базовая валюта', font=('Arial', 10, 'bold')).pack(pady=(15, 2))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.set('USD')  # Значение по умолчанию
base2_combobox.pack(pady=3, padx=10)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label(text=currencies['USD'])
base2_label.pack()

# Целевая валюта
Label(root, text='Целевая валюта', font=('Arial', 10, 'bold')).pack(pady=(15, 2))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.set('RUB')  # Значение по умолчанию
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_target_label)
target_label = ttk.Label(text=currencies['RUB'])
target_label.pack()

Button(text='Получить курс обмена', command=exchange).pack(pady=20)

root.mainloop()
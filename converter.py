import tkinter as tk

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        exchange_rates = {'Долар': 38.18, 'Євро': 41.81, 'Фунт': 49.12, 'Єна': 110.0, 'Гривня': 28.0}

        converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])

        result_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')

    except ValueError:
        result_label.config(text='Введіть коректну суму')

root = tk.Tk()
root.title('Конвертер валют')

label_amount = tk.Label(root, text='Сума:')
label_amount.grid(row=0, column=0, padx=10, pady=10)

entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

label_from_currency = tk.Label(root, text='Валюта з:')
label_from_currency.grid(row=1, column=0, padx=10, pady=10)

combo_from_currency = tk.Entry(root)
combo_from_currency.grid(row=1, column=1, padx=10, pady=10)
combo_from_currency.insert(0, 'Долар')  

label_to_currency = tk.Label(root, text='Валюта в:')
label_to_currency.grid(row=2, column=0, padx=10, pady=10)

combo_to_currency = tk.Entry(root)
combo_to_currency.grid(row=2, column=1, padx=10, pady=10)
combo_to_currency.insert(0, 'Гривня')

convert_button = tk.Button(root, text='Конвертувати', command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text='')
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

from tkinter import messagebox

import requests
from tkinter import *

class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

            # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return '{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)

    # Driver code
if __name__=='__main__':
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', "79c2b4068171f2132bac14159f1ad40f")
    c = Currency_convertor(url)

    window = Tk()
    window.title("Welcome to Currency Converter")

    window.geometry('400x300')

    lbl = Label(window, text="ENTER IN CAPITAL LETTERS")
    lbl.grid(column=0, row=0)

    lbl1 = Label(window, text="From Country")
    lbl1.grid(column =0, row=1)
    txt1 = Entry(window, width=10)
    txt1.grid(column=5, row=1)
    txt2 = Entry(window, width=10)
    txt2.grid(column=5, row=7)
    lbl2 = Label(window, text="TO Country")
    lbl2.grid(column=0, row=7)
    txt3 = Entry(window, width=10)
    txt3.grid(column=5, row=9)
    lbl3 = Label(window, text="Amount")
    lbl3.grid(column=0, row=9)


    def clicked():
        from_country = txt1.get()
        to_country = txt2.get()
        amount = int(txt3.get())
        a = c.convert(from_country, to_country, amount)
        Res = Label(window, text=a,bg="gray")
        Res.grid(column=5, row=20)


    btn = Button(window, text="Convert", command=clicked)
    btn.grid(column=5, row=12)

    window.mainloop()

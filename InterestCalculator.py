from tkinter import *

root = Tk()
root.title("Interest Calculator")

def compound():
    initial = Entry(root, width=75)
    initial.grid(row=2, column=0)
    initial.insert(0, "What amount of money are you putting in your account? ")

    rate = Entry(root, width=75)
    rate.grid(row=3, column=0)
    rate.insert(0, "What is your interest rate? ")

    number = Entry(root, width=75)
    number.grid(row=4, column=0)
    number.insert(0, "How many times is your interest compounded per year? ")

    time = Entry(root, width=75)
    time.grid(row=5, column=0)
    time.insert(0, "How many years are you saving your money? ")
    def calculate():
        P = int(initial.get())
        r = float(rate.get()) / 100
        n = int(number.get())
        t = int(time.get())
        Inside = (r / n) + 1
        exponent = (n * t)
        x = Inside ** exponent
        Amount = (P * x)
        amountlabel = Label(root, text=(round(Amount, 2)))
        amountlabel.grid(row=7, column=0)
    calculatebutton = Button(root, text="Calculate", command=calculate)
    calculatebutton.grid(row=6, column=0)

def simple():
    initial = Entry(root, width=75)
    initial.grid(row=2, column=2)
    initial.insert(0, "What amount of money are you putting in your account? ")

    rate = Entry(root, width=75)
    rate.grid(row=3, column=2)
    rate.insert(0, "What is your interest rate? ")

    time = Entry(root, width=75)
    time.grid(row=4, column=2)
    time.insert(0, "How many years are you saving your money? ")

    def calculate():
        P = int(initial.get())
        r = float(rate.get()) / 100
        t = int(time.get())
        Inside = (r * t) + 1
        Amount = P * Inside
        amountlabel = Label(root, text=(round(Amount, 2)))
        amountlabel.grid(row=6, column=2)

    calculatebutton = Button(root, text="Calculate", command=calculate)
    calculatebutton.grid(row=5, column=2)


mylabel = Label(root, text="    Is your interest Compound or Simple?    ")
mylabel.grid(row=0, column=1)

myButton1 = Button(root, text="Compound", padx=25, pady=25, command=compound)
myButton1.grid(row=1, column=0)\

myButton2 = Button(root, text="Simple", padx=25, pady=25, command=simple)
myButton2.grid(row=1, column=2)

root.mainloop()

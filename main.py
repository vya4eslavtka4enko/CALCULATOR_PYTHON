import tkinter
from tkinter import *
from tkinter import ttk
import math



class Calculator():
    def __init__(self):

        self.memory = ''

        self.entry = tkinter.Entry(window, width=30, font=('Helvetica 64'))
        self.entry.grid(row=0, column=0, columnspan=3,pady = 15)

        sum_button = Button(window, text="+", height=2, width=4, command=self.sum).grid(row=2, column=0, padx=1, pady=2)
        subtraction_button = Button(window, text="-", height=2, width=4, command=self.subtraction).grid(row=2, column=1,padx=2, pady=2)
        multiplication_button = Button(window, text="*", height=2, width=4, command=self.multiplication).grid(row=2,column=2,padx=2,pady=2)
        division_button = Button(window, text="/", height=2, width=4, command=self.division).grid(row=3, column=0)
        clear_button = Button(window, text="C", height=2, width=4, fg='red',command=self.clear).grid(row=3, column=1)
        square_root = Button(window, text="√", height=2, width=4,command=self.square_root).grid(row=3, column=2)

        self.one = Button(window, text='1', height=2, width=4, command=lambda:self.write_number(self.one))
        self.one.grid(row=4, column=0, padx=2, pady=2)

        self.two = Button(window, text='2', height=2, width=4, command=lambda:self.write_number(self.two))
        self.two.grid(row=4, column=1, padx=2, pady=2)

        self.three = Button(window, text='3', height=2, width=4, command=lambda:self.write_number(self.three))
        self.three.grid(row=4, column=2, padx=2, pady=2)

        self.four = Button(window, text='4', height=2, width=4, command=lambda:self.write_number(self.four))
        self.four.grid(row=5, column=0, padx=2, pady=2)

        self.five = Button(window, text='5', height=2, width=4, command=lambda:self.write_number(self.five))
        self.five.grid(row=5, column=1, padx=2, pady=2)

        self.six = Button(window, text='6', height=2, width=4, command=lambda:self.write_number(self.six))
        self.six.grid(row=5, column=2, padx=2, pady=2)

        self.seven = Button(window, text='7', height=2, width=4, command=lambda:self.write_number(self.seven))
        self.seven.grid(row=6, column=0, padx=2, pady=2)

        self.eight = Button(window, text='8', height=2, width=4, command=lambda:self.write_number(self.eight))
        self.eight.grid(row=6, column=1, padx=2, pady=2)

        self.nine = Button(window, text='9', height=2, width=4, command=lambda:self.write_number(self.nine))
        self.nine.grid(row=6, column=2, padx=2, pady=2)

        self.zero = Button(window, text='0', height=2, width=4, command=lambda:self.write_number(self.zero))
        self.zero.grid(row=7, column=1, padx=2, pady=2)

        percentege = Button(window, text="%", height=2, width=4, command=self.percentege).grid(row=7, column=0)
        equals = Button(window, text="=", height=2, width=4, command=self.equals).grid(row=7, column=2)

    def division(self):
        x1 = self.entry.get()
        self.entry.delete(0,'end')
        self.memory = f'{x1} /'

    def multiplication(self):
        x1 = self.entry.get()
        self.entry.delete(0, 'end')
        self.memory = f'{x1} *'


    def sum(self):
        x1 = self.entry.get()
        self.entry.delete(0, 'end')
        self.memory = f'{x1} +'


    def subtraction(self):
        x1 = self.entry.get()
        self.entry.delete(0, 'end')
        self.memory = f'{x1} -'


    def equals(self):
        x2 = self.entry.get()
        list_operation = self.memory.split(' ')
        if list_operation[1] == '*':

            result = int(list_operation[0]) * int(x2)
            print(result)
            self.entry.delete(0, 'end')
            self.entry.insert(10,f"{result}")

        elif list_operation[1] == "/":

            result = int(list_operation[0]) / int(x2)
            print(result)
            self.entry.delete(0, 'end')
            self.entry.insert(10, f"{result}")

        elif list_operation[1] == '-':

            result = int(list_operation[0]) - int(x2)
            print(result)
            self.entry.delete(0, 'end')
            self.entry.insert(10, f"{result}")

        elif list_operation[1] == "+":

            result = int(list_operation[0]) + int(x2)
            print(result)
            self.entry.delete(0, 'end')
            self.entry.insert(10, f"{result}")

        elif list_operation[1] == "%":

            result = int((list_operation[0]) / (float(x2) / 100))
            print(float(x2) / 100)
            self.entry.delete(0,'end')
            self.entry.insert(10,f'{result}')

    def write_number(self,text):
        self.entry.insert(10,text["text"])

    def square_root(self):
        result = math.sqrt(int(self.entry.get()))
        self.entry.insert(0, result)


    def percentege(self):
        x1 = self.entry.get()
        self.entry.delete(0, 'end')
        self.memory = f'{x1} *'


    def clear(self):
        self.entry.delete(0,'end')


if __name__ == "__main__":
    window = Tk();
    window.geometry("270x400")
    window.resizable(False,False)
    window.columnconfigure(1, weight=50)
    window.rowconfigure(1, weight=50)

    calc = Calculator()



    window.mainloop()
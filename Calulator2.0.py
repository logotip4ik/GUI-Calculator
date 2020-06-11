from tkinter import *
import subprocess
from tkinter import messagebox as mb

class Tokenize:
    def __init__(self, string):
        self.string = string+'='
        self.op = ['+', '-', '*', '/', '=']
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        number = ''
        for item in self.string:
            try:
                int(item)
                number += str(item)
            except ValueError:
                if item in self.op:
                    self.tokens.append(str(number))
                    number = ''
                    self.tokens.append(str(item))
                elif item == ' ':
                    pass
                else:
                    return mb.showerror("Wrong input", f"This is wrong: {str(item)}")


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("294x370")
        self.root.resizable(0, 0)
        self.root.config(background='#dbdbdb')
        self.root.bind("<Return>", lambda x: self.eq())
        self.initUI()
        self.entry.focus()
        self.b_eq.bind("<Return>", self.eq)

    def insert(self, symbol):
        self.entry.insert(END, symbol)

    def ac(self):
        self.entry.delete(0, END)

    def eq(self):
        tokens = Tokenize(self.entry.get()).tokens[:-1]
        output = subprocess.run(["python", "-c", f"print({''.join(tokens)})"], stdout=subprocess.PIPE)
        result = output.stdout.decode('utf-8')
        self.entry.insert(END, result)

    def erase(self):
        self.entry.delete(len(self.entry.get()) - 1, END)

    def initUI(self):
        self.entry = Entry(self.root, width=10, relief='solid', justify=LEFT, font=("Courier", 36))
        self.entry.grid(row=0, columnspan=4)
        self.b_0 = Button(self.root, text="0", font=("Courier", 24), width=7, command=lambda: self.insert(0))
        self.b_0.grid(columnspan=2, row=5)
        self.b_1 = Button(self.root, text="1", font=("Courier", 24), width=3, command=lambda: self.insert(1))
        self.b_1.grid(column=0, row=4)
        self.b_2 = Button(self.root, text="2", font=("Courier", 24), width=3, command=lambda: self.insert(2))
        self.b_2.grid(column=1, row=4)
        self.b_3 = Button(self.root, text="3", font=("Courier", 24), width=3, command=lambda: self.insert(3))
        self.b_3.grid(column=2, row=4)
        self.b_4 = Button(self.root, text="4", font=("Courier", 24), width=3, command=lambda: self.insert(4))
        self.b_4.grid(column=0, row=3)
        self.b_5 = Button(self.root, text="5", font=("Courier", 24), width=3, command=lambda: self.insert(5))
        self.b_5.grid(column=1, row=3)
        self.b_6 = Button(self.root, text="6", font=("Courier", 24), width=3, command=lambda: self.insert(6))
        self.b_6.grid(column=2, row=3)
        self.b_7 = Button(self.root, text="7", font=("Courier", 24), width=3, command=lambda: self.insert(7))
        self.b_7.grid(column=0, row=2)
        self.b_8 = Button(self.root, text="8", font=("Courier", 24), width=3, command=lambda: self.insert(8))
        self.b_8.grid(column=1, row=2)
        self.b_9 = Button(self.root, text="9", font=("Courier", 24), width=3, command=lambda: self.insert(9))
        self.b_9.grid(column=2, row=2)
        self.b_eq = Button(self.root, text='=', font=("Courier", 24), width=3, command=self.eq)
        self.b_eq.grid(column=3, row=5)
        self.b_plus = Button(self.root, text='+', font=("Courier", 24), width=3, command=lambda: self.insert('+')).grid(column=3, row=4)
        self.b_minus = Button(self.root, text='-', font=("Courier", 24), width=3, command=lambda: self.insert('-')).grid(column=3, row=3)
        self.b_multip = Button(self.root, text='*', font=("Courier", 24), width=3, command=lambda: self.insert('*')).grid(column=3, row=2)
        self.b_devide = Button(self.root, text='/', font=("Courier", 24), width=3, command=lambda: self.insert('/')).grid(column=3, row=1)
        self.b_ac = Button(self.root, text='AC', font=("Courier", 24), width=7, command=self.ac).grid(columnspan=2, column=0, row=1)
        self.b_point = Button(self.root, text='.', font=("Courier", 24), width=3, command=lambda: self.insert('.')).grid(column=2, row=5)
        self.b_back = Button(self.root, text='<-', font=("Courier", 24), width=3, command=self.erase).grid(column=2, row=1)


if __name__ == '__main__':
    window = Tk()
    root = MainWindow(window)
    window.mainloop()

__version__ = 2.0

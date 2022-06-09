import tkinter as tk
from tkinter import *

def rootWindow():

    def case1():
        global choise, window
        window.destroy()
        choise = 1

    def case2():
        global choise, window
        window.destroy()
        choise = 2

    def case3():
        global choise, window
        window.destroy()
        choise = 3


    def rootWindowConfig():
        global window
        window = tk.Tk()
        window.geometry('300x180')
        window.resizable(False, False)
        window.title('Телефонная книга')

        frame = Frame(window)
        addButton = Button(frame, text='Добавить контакт', pady=5, padx=5, width=20, command=lambda: case1())
        delButton = Button(frame, text='Удалить контакт', pady=5, padx=5, width=20, command=lambda: case2())
        viewButton = Button(frame, text='Посмотреть контакты', pady=5, padx=5, width=20, command=lambda: case3())

        frame.grid(row=0, column=0)
        addButton.grid(row=0, column=0, sticky='ns', padx=70, pady=10)
        delButton.grid(row=1, column=0, sticky='ns', pady=10)
        viewButton.grid(row=2, column=0, sticky='ns', pady=10)

        window.mainloop()

    global choise
    choise = None
    rootWindowConfig()
    return choise

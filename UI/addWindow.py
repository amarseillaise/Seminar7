import tkinter as tk
from tkinter import *


def makeWindow():
    def makeWindowConfigure():
        global windowAdd, nameVar, phoneVar
        windowAdd = tk.Tk()
        windowAdd.geometry('300x120')
        windowAdd.resizable(False, False)
        windowAdd.title('Добавить контакт')

        frame = Frame(windowAdd)
        nameLabel = Label(frame, text='ФИО')
        phoneLabel = Label(frame, text='Телефон')
        nameVar = StringVar(frame)
        nameEntry = Entry(frame, width=30, textvariable=nameVar)
        phoneVar = StringVar(frame)
        phoneEntry = Entry(frame, width=30, textvariable=phoneVar)
        doneButton = Button(frame, text='Готово', width=7, command=lambda: windowAdd.destroy())

        frame.grid(row=0, column=0)
        nameLabel.grid(row=0, column=0, pady=10, padx=30)
        phoneLabel.grid(row=1, column=0, pady=10)
        nameEntry.grid(row=0, column=1, pady=10)
        phoneEntry.grid(row=1, column=1, pady=10)
        doneButton.grid(row=2, column=0, columnspan=2, padx=1, pady=5)

        windowAdd.mainloop()

    global nameVar, phoneVar
    makeWindowConfigure()
    return str(nameVar.get()), str(phoneVar.get())

import tkinter as tk
from tkinter import *


def windowDelete():
    def windowDeleteConfigure():
        global idVar
        windowRemove = tk.Tk()
        windowRemove.geometry('260x120')
        windowRemove.resizable(False, False)
        windowRemove.title('Удалить контакт')

        frame = Frame(windowRemove)
        infoLabel = Label(frame, text='Введите ID контакта, который нужно удалить')
        idVar = IntVar(frame)
        idSpin = Spinbox(frame, textvariable=idVar, from_=1, to=100, width=5)
        doneButton = Button(frame, text='Удалить', command=windowRemove.destroy)

        frame.grid(row=0, column=0)
        infoLabel.grid(row=0, column=0, pady=5)
        idSpin.grid(row=1, column=0, pady=5)
        doneButton.grid(row=2, column=0, pady=5)

        windowRemove.mainloop()

    global IdVar
    windowDeleteConfigure()
    return int(idVar.get())

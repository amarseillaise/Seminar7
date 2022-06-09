import tkinter as tk
from tkinter import *


def demoWindow(bd):
    def demoWindowConfigure(bd):
        roww = 0
        windowDemo = tk.Tk()
        windowDemo.geometry('400x500')
        windowDemo.resizable(False, False)
        windowDemo.title('Просмотреть контакты')

        frame = Frame(windowDemo)
        nameLabel = Label(frame, text='ФИО')
        phoneLabel = Label(frame, text='Телефон')
        idLabel = Label(frame, text='ID')
        doneButton = Button(frame, text='Назад', width=7, command=lambda: windowDemo.destroy())

        frame.grid(row=roww, column=0)
        idLabel.grid(row=roww, column=0, pady=10, padx=30)
        nameLabel.grid(row=roww, column=1, pady=10, padx=50)
        phoneLabel.grid(row=roww, column=2, pady=10, padx=55)

        roww += 1
        for note in range(len(bd)):
            currentNote = bd[note].split(';')
            Label(frame, text=currentNote[0]).grid(row=roww, column=0, pady=1)
            Label(frame, text=currentNote[1]).grid(row=roww, column=1, pady=1)
            Label(frame, text=currentNote[2]).grid(row=roww, column=2, pady=1)
            roww += 1

        doneButton.grid(row=roww, column=2, padx=1, pady=5)

        windowDemo.mainloop()

    demoWindowConfigure(bd)
    return 'showed'

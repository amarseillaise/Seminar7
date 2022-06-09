import os
import pathlib


def addToBd(name, phone):
    file = str(pathlib.Path(os.getcwd())) + '\\BD\\BD.txt'
    with open(file, 'r') as check:
        lastId = int(str(check.read()).split('\n')[-2][0])
    with open(file, 'a') as bd:
        bd.write(f'{lastId + 1};{name};{phone}\n')
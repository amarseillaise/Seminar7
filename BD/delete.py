import os
import pathlib


def delFromBd(id):
    file = str(pathlib.Path(os.getcwd())) + '\\BD\\BD.txt'
    with open(file, 'r') as bd:
        data = str(bd.read()).split('\n')[:-1]
    for i in range(len(data)):
        if int(data[i].split(';')[0]) == int(id):
            del data[i]
            break
    with open(file, 'w') as bdw:
        for j in data:
            bdw.write(f'{str(j)}\n')

import os
import pathlib


def getBd():
    file = str(pathlib.Path(os.getcwd())) + '\\BD\\BD.txt'
    with open(file, 'r') as bd:
        importt = bd.read().split('\n')[:-1]
    return importt
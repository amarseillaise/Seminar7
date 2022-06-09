from .mainWindow import rootWindow
from .addWindow import makeWindow
from .showWindow import demoWindow
from .delWindow import windowDelete
from BD import get


def Managing():
    action = rootWindow()
    if action == 1:
        return makeWindow()
    elif action == 3:
        return demoWindow(get.getBd())
    elif action == 2:
        return windowDelete()

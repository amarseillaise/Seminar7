from UI import windowsManager
from BD import set, delete


def Launch():
    while True:
        managerAction = windowsManager.Managing()
        if isinstance(managerAction, tuple):
            set.addToBd(managerAction[0], managerAction[1])
        elif managerAction == 'showed':
            continue
        elif isinstance(managerAction, int):
            delete.delFromBd(managerAction)
        else:
            raise SystemExit

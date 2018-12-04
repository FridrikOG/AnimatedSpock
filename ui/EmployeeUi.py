


import time

class EmployeeUi():
    def __init__(self):
        pass
    def startPageMenu(self):
        action = True
        while action:
            startPageMenuPrint()
            action = startPageMenuAction()

        
def startPageMenuPrint():
    print("--------Start-Page--------")
    print("3. Register customer.")



def startPageMenuAction():
    action = '1'
    if action == '1':
        print("1.")
    if action == 'q':
        print('Exiting program!')

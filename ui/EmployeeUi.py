from models.Customer import Customer

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
    action = '3'
    if action == '3':
        print("3")

def main():
    ui = EmployeeUi()
    ui.startPageMenu()

main()
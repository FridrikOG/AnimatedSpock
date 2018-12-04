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

def createCustomer():
    name = input('Enter name: ')
    age = input('Enter age: ')
    ssn = input('Enter Social-security-nr: ')
    return name,age,ssn


def startPageMenuAction():
    action = '3'
    if action == '3':
        name,age,ssn = createCustomer()
        newCustomer = Customer(name,age,ssn)
        
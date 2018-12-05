from services.CustomerService import CustomerService
from models.Customer import Customer


class EmployeeUi():
    def __init__(self):
        self.__customerService = CustomerService()

    def startPageMenu(self):
        action = True
        while action:
            mainMenuPrint()
            action = '3'
            if action == '3':
                name,age,ssn = createCustomer()
                newCustomer = Customer(name,age,ssn)
                self.__customerService.addCustomer(newCustomer)

        
def mainMenuPrint():
    print("\nYou can do the following: ")
    print("1. List all available cars")
    print("2. List all unavailable cars")
    print("3. Register customer.")
    print("4. Create car reservation.")
    print("5. Find a customer.")
    print("6. Look up an order.")
    print("7. Show list of orders.")
    print("8. Return a car.")
    print("9. Edit order.")
    print("press q to quit\n")

def createCustomer():
    name = input('Enter name: ')
    age = input('Enter age: ')
    ssn = input('Enter Social-security-nr: ')
    return name,age,ssn
        
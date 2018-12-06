from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer


class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()


    def findCustomerMenu(self):
            findCustomerAction = input('Choose action: ')
            if findCustomerAction == '0':
                self.mainMenu()
            elif findCustomerAction == '1':
                self.searchCustomerPrintHeader()
                searchTerm = input("Input SSN or name to find: ")
                self.displayCustomerHeaderPrint()
                self.__customerService.findCustomer(searchTerm)
                
            elif findCustomerAction == '2':
                customers = self.__customerService.getAllCustomers()
                self.displayAllCustomersPrint(customers)

    def mainMenu(self):
        action = ''
        while action != 'q':
            self.mainMenuPrint()
            action = input('Action: ')

            if action == '1' or action == '2':
                cars = self.__carService.getCars(action)
                self.displayAllCarsPrint(cars)

            if action == '3':
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)

            elif action == '5':
                self.findCustomerMenuPrint()
                self.findCustomerMenu()


    def mainMenuPrint(self):
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

    def createCustomer(self):
        print("-----------Creating customer account-----------")
        cs = CustomerService()
        name = cs.inputNameCheck()
        age = cs.inputAgeCheck()
        ssn = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = self.countingCustomers()
        number += 1
        return name,age,ssn, address, number

    # Displays options that the user has.
    def findCustomerMenuPrint(self):
        print("0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")

    def displayCustomerHeaderPrint(self):
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "---------------", "---------------"))

    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)
    
    def displayAllCarsPrint(self,cars):
        LINE = '---------------'
        print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))
        for car in cars:
            print(car)
        

    def searchCustomerPrintHeader(self):
        print("--------------------------------------------Search for customer-------------------------------------------")

#Checking if ssn consists of 10 integers
    def errorCheckingSsn(self):
        ssn = ''
        while len(str(ssn)) != 10:
            try:
                ssn = int(input("Step 3/5 - Enter an SSN of 10 numbers: "))
            except ValueError:
                print("Please enter only 10 integers")
        return ssn

    def countingCustomers(self):
        listOfSsn = self.__customerService.countingCustomers()
        return len(listOfSsn)

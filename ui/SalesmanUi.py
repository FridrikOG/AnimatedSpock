from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Order import Order
from services.OrderService import OrderService
from datetime import datetime, timedelta
from models.Colors import Colors



class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()
        self.__orderService = OrderService()

    def mainMenu(self):
        action = ''
        while action != 'q':
            self.spaces()
            self.mainMenuPrint()
            action = self.chooseAction()

            if action == '1' or action == '2':
                self.spaces()
                typeAction = ''
                dateAvailable = datetime.now()
                if action == '1':
                    self.allAvailableCars()
                    print("\nPath: Menu/Available_Cars/")
                elif action == '2':
                    print("\nPath: Menu/UnAvailable_Cars/")
                    self.allUnAvilableCars()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)

            
# Find a customer
            elif action == '3':
                self.spaces()
                self.findCustomerMenu()
# Register a customer
            elif action == '4':
                self.spaces()
                print("\nPath: Menu/Creating_Customer/\n")
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)
                print("\nCustomer has been created!\n")
                self.displayCustomerHeaderPrint()
                print(str(newCustomer))
                action = self.pressEnterToContinue()

# Create a car order
            elif action == '5':
                self.spaces()
                print("\nPath: Menu/Create_Car_Order/")
                self.createOrder()
# Lookup an Order
            elif action == '6':
                self.spaces()
                print("\nPath: Menu/Look_Up_Order/")

                self.editOrderInfoMenu()

# Show a list of orders
            elif action == '7':
                self.spaces()
                print("\nPath: Menu/List_Of_All_Orders/")
                orders, nothing = self.__orderService.getAllOrders()
                self.displayAllOrders(orders)
                self.pressEnterToContinue()
                #print all orders and options
# Rent out a car
            elif action == '8':
                self.spaces()
                print("\nPath: Menu/List_Of_Available_Cars/")
                ######display available cars header#####
                # display available cars
                cars = self.__carService.getCars('1', '', datetime.now())
                self.displayAllCarsPrint(cars)
                # rent out a car funcion
                self.rentOutACar()
# Return a car
            elif action == '9':
                self.spaces()
                self.returnCar()

# Register a car
            elif action == '10':
                self.spaces()
                print("\nPath: Menu/Register_New_Car/")
                newCar = self.createCar()
                self.__carService.addCar(newCar)
# Edit a car
            elif action == '11':
                self.spaces()
                print("\nPath: Menu/Edit_Car/")
                self.editCar()

# Prints out the pricelist for cars.
            elif action == '12':
                self.spaces()
                print("\nPath: Menu/Pricelist/")
                print(open('./data/pricelist.txt').read())
                action = self.pressEnterToContinue()

# Prints exit message and exits the program.
            elif action == 'q':
                self.spaces()
                self.exitPrint()
                exit()
# unwanted action gets recognized and gives feedback to the user.
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.mainMenu()

# Prints the mainMenuPage.
    def mainMenuPrint(self):
        self.spaces()
        print("___  ___     _       ___  ___")
        print("|  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ ")
        print("| |\/| / _` | | ' \  | |\/| / -_) ' \ || |")
        print("|_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|")
        print("\nPath: Menu/\n")
        print("You can do the following:")
        print("1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Find a customer")
        print("4.  Register customer")
        print("5.  Create a car order")
        print("6.  Look up an order")
        print("7.  Show list of orders")
        print("8.  Rent out a car")
        print("9.  Return a car")
        print("10. Register car")
        print("11. Edit a car")
        print("12. Pricelist for cars.")
        print("Press q to quit\n")
    

    '''----------Functions for repetitive code-----------'''
    def spaces(self):
        print('\n'*50)

    def chooseAction(self):
        action = input("\nChoose action: ").strip()
        return action

    def pressEnterToContinue(self):
        action = input("\nPress enter to continue: ").strip()
        return action

    def actionsPrint(self):
        print("\n" + "Actions: ")

    def customerFound(self):
        print("Customer found!\n")

    def customerNotFound(self):
        print("\nCustomer not found!")

    def searchTermInput(self):
        searchTerm = input("\nEnter SSN or Customer number to find: ").strip()
        return searchTerm

    def exitPrint(self):
        print("\nHave a nice day!")
        print("Exiting program..")

    def allCustomersHeaderPrint(self):
        print(
        "---------------------------------------------- All Customers ----------------------------------------------\n"
        )

    def allDeletedCustomerHeaderPrint(self):
        print(
        "---------------------------------------------- All Deleted Customers ----------------------------------------------\n"
        )

    def allAvailableCars(self):
        print(
        "---------------------------------------------- ALL Available Cars ----------------------------------------------\n"
        )

    def allUnAvilableCars(self):
        print(
        "--------------------------------------------- ALL Unavailable Cars ---------------------------------------------\n"
        )

    def creatingCustomerPrintHeader(self):
        print(
        "--------------------------------------------- Create a Customer Account ---------------------------------------------"
       )

    def invalidAction(self,action):
        print("\nAction "+f"'{action}'"+" is not a valid action!")
        # else:
        # self.invalidAction(action)
        # self.pressEnterToContinue()
        # self.showCarsByTypeMenu(typeAction,dateAvailable)

    ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.findCustomerMenuPrint()
        action = self.chooseAction()

# Redirects the user to the mainMenuPage.
        if action == '0':
            self.mainMenu()

# Search engine that finds the customer.
        elif action == '1':
            print("Path: Menu/Find_Customer/Search_For_A_Customer/")
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                print("Path: Menu/Find_Customer/Not_Found/\n")
                self.customerNotFound()
                self.pressEnterToContinue()
                self.findCustomerMenu()
    
# If the customer is found it prints found message.
            else:
                print("Path: Menu/Find_Customer/Selected_Customer/\n")
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print((str(customer)))
                self.afterCustomerIsFoundMenu(customer)
#show all customers
        elif action == '2':
            print("Path: Menu/Find_Customer/All_Customers/\n")
            self.allCustomersHeaderPrint()
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressEnterToContinue()
            self.findCustomerMenu()

# Shows all deleted customers.
        elif action == '3':
            print("Path: Menu/Find_Customer/All_Deleted_Customers/\n")
            self.allDeletedCustomerHeaderPrint()
            customers = self.__customerService.getAllDeletedCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressEnterToContinue()
            self.findCustomerMenu()

# Search engine in the deleted customers dir.
        elif action == '4':            
            print("Path: Menu/Find_Customer/Search_Deleted/\n")
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findDeletedCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                self.customerNotFound()
                self.pressEnterToContinue()
                self.findCustomerMenu()
            
# If the customer is found it prints found message.
            else:
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print((str(customer)))
                self.afterDeletedCustomerIsFoundMenu(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.findCustomerMenu()

# After the customer is found the user can go back or reinstate the customer.
    def afterDeletedCustomerIsFoundMenu(self,customer):
        self.afterDeletedCustomerIsFoundPrint()
        action = self.chooseAction()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.reinstatingWarningMessageMenu(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.afterDeletedCustomerIsFoundMenu(customer)

    def reinstatingWarningMessageMenu(self,customer):
        
        self.reinstatingWarningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.restoringCustomer(customerNumber)
                print("Customer "+f"'{customer.getName()}'"+" has been reinstated.")  # Customer reinstated
                self.pressEnterToContinue()
                self.findCustomerMenu()
            elif action == '2':
                self.afterDeletedCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.reinstatingWarningMessageMenu(customer)

    def reinstatingWarningMessagePrint(self,customer):
        print("Path: Menu/Find_Customer/Selected_Customer/Reinstate_Selected_Customer/")
        print("\nSelected customer: ")
        self.displayCustomerHeaderPrint()
        print(str(customer))
        print("\nWarning: " + "Are you sure you want to reinstate this customer?")
        print("1. Yes, reinstate this customer")
        print("2. No, do not reinstate this customer")
        
# After the customer is found the user can go back and search another, edit or delete the customer.
    def afterCustomerIsFoundMenu(self, customer):
        self.afterCustomerIsFoundPrint()
        action = self.chooseAction()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.editCustomerInfo(customer)
        elif action == '2':
            self.warningMessageMenu(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.afterCustomerIsFoundMenu(customer)
    
            
# The menu for editing the customer information, Number stays the same
#Shows original name after editing again
    def editCustomerInfo(self,customer):
        self.editCustomerInfoPrint()
        cs = CustomerService()
        action = self.chooseAction()
        name = customer.getName()
        age = customer.getAge()
        ssn = customer.getSsn()
        address = customer.getAddress()
        number = customer.getNumber()
        if action =='0':
            self.afterCustomerIsFoundMenu(customer)
# Edit customer name
        elif action =='1':
            print("Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Name/\n")
            print("Editing customers name:")
            name = cs.inputNameCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print("\nCustomer name has been changed from "\
            +f"'{customer.getName()}'"+" to "+f"'{name}\n'")
            self.displayCustomerHeaderPrint()
            print(newCustomer)
            self.pressEnterToContinue()
            self.editCustomerInfo(newCustomer)
#Edit customer ssn
        elif action =='2':
            print("Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/SSN/\n")
            print("Editing customers SSN:")
            ssn,age = cs.inputSsnCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print("\nCustomer address has been changed from "\
            +f"'{customer.getSsn()}'"+" to "+f"'{ssn}\n'")
            self.displayCustomerHeaderPrint()
            print(newCustomer)
            self.pressEnterToContinue()
            self.editCustomerInfo(newCustomer)
#Edit customer address
        elif action =='3':
            print("Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Address/\n")
            print("Editing customers address:")
            address = cs.inputAddressCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print("\nCustomer address has been changed from "\
            +f"'{customer.getAddress()}'"+" to "+f"'{address}\n'")
            self.displayCustomerHeaderPrint()
            print(newCustomer)
            self.pressEnterToContinue()
            self.editCustomerInfo(newCustomer)

#Edit all customer information
        # elif action == '4':
        #     print("Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/All_Customer_Info/\n")
        #     print("Editing customers name, SSN and address:")
        #     cs = CustomerService()
        #     name = cs.inputNameCheck()
        #     ssn,age = cs.inputSsnCheck()
        #     address = cs.inputAddressCheck()
        #     newCustomer = Customer(name,age,ssn,address,number)
        #     cs.customerEdit(newCustomer)
        #     displayCustomerHeaderPrint()
        #     print(newCustomer)
        #     self.pressEnterToContinue()
        #     self.editCustomerInfo(newCustomer)
            
# Name changed
            print("\nCustomer address has been changed from "\
            +f"'{customer.getName()}'"+" to "+f"'{name}'")
# Ssn changed
            print("\nCustomer address has been changed from "\
            +f"'{customer.getSsn()}'"+" to "+f"'{ssn}'")
# Address changed
            print("\nCustomer address has been changed from "\
            +f"'{customer.getAddress()}'"+" to "+f"'{address}'")
            self.pressEnterToContinue()
            self.editCustomerInfo(newCustomer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.editCustomerInfo(newCustomer)

# Safety function that asks the user if he is certain that he wants to delete the selected customer.
    def warningMessageMenu(self,customer):
        self.warningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                print("Customer "+f"'{customer.getName()}'"+" has been deleted.") # Customer Deleted
                self.pressEnterToContinue()
                self.findCustomerMenu()
            elif action == '2':
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.warningMessageMenu(customer)

        
# Creates a customer, calls a function in the service class to validate the input.
    def createCustomer(self):
        self.creatingCustomerPrintHeader()
        cs = CustomerService()
        name = cs.inputNameCheck()
        ssn, age = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.getSumOfAllCustomers()
        action = ''
        while action != '1' or action != '2':
            self.createCustomerCheckPrint()
            action = self.chooseAction()
            if action == '1':
                return name,age,ssn,address,number
            elif action == '2':
                self.mainMenu()
            self.invalidAction(action)
            self.pressEnterToContinue()

    def createCustomerCheckPrint(self):
        print("\nDo you want to create this customer?")
        print("1. Yes, I want to create this customer")
        print("2. No, I don't want to create this customer")


    '''-------------------------- CUSTOMER PRINT FUNCTIONS -----------------------'''
# Actions the user has after 5 is pressed on the mainPage.
    def findCustomerMenuPrint(self):
        print("Path: Menu/Find_Customer/")
        print(
        "-------------------------------------------- Find a Customer -------------------------------------------"
        
       )
        self.actionsPrint()
        print("0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")
        print("3. Show all deleted customers")
        print("4. Search for deleted customer")

# The format which the customer is printed out on.
    def displayCustomerHeaderPrint(self):
        print("{:24} {:15} {:15} {:20} {:<15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("-----------------------",\
        "---------------","---------------", "--------------------", "---------------"))
# Comes after the displayCustomerHeaderPrint, prints out all the customers.
    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print((str(customer)))
    
# Header which is printed when user is searching for a customer.
    def searchCustomerHeaderPrint(self):
        print(
        "------------------------------------------ Search for a Customer ----------------------------------------"
       )

# Prints the option to go back or reinstate the customer back into the main customer dir file.   VANTAR PATH
    def afterDeletedCustomerIsFoundPrint(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Re-instate selected customer")

# 
    def afterCustomerIsFoundPrint(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer")

# Print function that displays users action choice.
    def editCustomerInfoPrint(self):
        print("Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/")
        self.actionsPrint()
        print("0. <-- Go back")
        print("1. Edit customer name")
        print("2. Edit customer SSN")
        print("3. Edit customer address")
       # print("4. Edit All customer information")

# Prints when user chooses to delete a user.
    def warningMessagePrint(self,customer):
        print("Path: Menu/Find_Customer/Selected_Customer/Deleted_Selected_Customer/")
        print("\nSelected customer: ")
        self.displayCustomerHeaderPrint()
        print((str(customer)))
        print("\nWarning: " + "Are you sure you want to delete this customer?")
        print("1. Yes, delete this customer")
        print("2. No, do not deleted this customer")
    
    
    
    ''' -------------------- CAR FUNCTIONS -------------------- '''

    def editCarMenuPrint(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Car Type")
        print("2. Make")
        print("3. Color")
        print("4. Passenger")
        print("5. Transmission")

    def editCar(self):
        print("-------------------------------------------------- Edit a Car --------------------------------------------------")
        licensePlate = self.__carService.checkLicenseplate(False)
        searchedCar = self.__carService.licensePlateCheck(licensePlate)
        if searchedCar == None:
            print("\nCar not found!")
            self.pressEnterToContinue()
            self.editCar()
            return False
        self.printCarHeader()
        print(searchedCar)
        carType = searchedCar.getType()
        make = searchedCar.getMake()
        color = searchedCar.getColor()
        passengers = searchedCar.getPassengers()
        transmission = searchedCar.getTransmission()
        rentCost = searchedCar.getRentcost()
        status = searchedCar.getStatus()
        rentOutCar = searchedCar.getRentOutCar()
        self.editCarMenuPrint()
        action = self.chooseAction()
        if action == '0':
            #Go back
            self.editCar()
        elif action == '1':
            #Edit car type
            print("\nPath: Menu/Edit_Car/Edit_Car_Type/")     
            self.selectCarTypePrintMenu()       
            carTypeInput = self.__carService.checkCarType()
            rentCost, carType = self.getCarTypeVariables(carTypeInput)
        elif action == '2':
            #Edit make
            print("\nPath: Menu/Edit_Car/Edit_Make/")
            make = input('Make (f.x. Toyota Yaris): ').strip().capitalize()
        elif action == '3':
            #Edit color
            print("\nPath: Menu/Edit_Car/Edit_Color/")
            color = input('Color: ').strip().capitalize()
        elif action == '4':
            #Edit passengers
            print("\nPath: Menu/Edit_Car/Edit_Passengers/")
            passengers = self.__carService.checkPassengers()
        elif action == '5':
            #Edit Transmission
            print("\nPath: Menu/Edit_Car/Edit_Transmission/")
            transmissionInput = self.__carService.checkTransmission()
            transmission = self.getTransmission(transmissionInput)
        rentOutCar, unusedValue = self.getTimeOfOrder()
        returnCar = rentOutCar
        editedCar = self.__carService.editCar(carType,make,licensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        print("\nCar successfully edited!")
        self.printCarHeader()
        print(str(editedCar))
        self.pressEnterToContinue()

    def showCarsByTypeMenu(self, typeAction,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            action = self.chooseAction()
            if action == '0':
                self.mainMenu()
            elif action == '1':
                if typeAction == '1':
                    print("\nPath: Menu/Available_Cars/Compact/")
                    self.allAvailableCars()
                elif typeAction == '2':
                    print("\nPath: Menu/UnAvailable_Cars/Compact/")
                    self.allUnAvilableCars()
                action = 'compact'
            elif action == '2':
                if typeAction == '1':
                    print("\nPath: Menu/Available_Cars/Comfort/")
                    self.allAvailableCars()
                elif typeAction == '2':
                    print("\nPath: Menu/UnAvailable_Cars/Comfort/")
                    self.allUnAvilableCars()
                action = 'comfort'
            elif action == '3':
                if typeAction == '1':
                    print("\nPath: Menu/Available_Cars/CUV/")
                    self.allAvailableCars()
                elif typeAction == '2':
                    print("\nPath: Menu/UnAvailable_Cars/CUV/")
                    self.allUnAvilableCars()
                action = 'CUV'
            elif action == '4':
                if typeAction == '1':
                    print("\nPath: Menu/Available_Cars/Highland/")
                    self.allAvailableCars()
                elif typeAction == '2':
                    print("\nPath: Menu/UnAvailable_Cars/Highland/")
                    self.allUnAvilableCars()
                action = 'highland'
            elif action == '5':
                if typeAction == '1':
                    print("\nPath: Menu/Available_Cars/Luxury/")
                    self.allAvailableCars()
                elif typeAction == '2':
                    print("\nPath: Menu/UnAvailable_Cars/Luxury/")
                    self.allUnAvilableCars()
                action = 'luxury'
            elif action == '6':
                self.rentOutACar()
                return False
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.showCarsByTypeMenu(typeAction,dateAvailable)
            cars = self.__carService.getCars(typeAction, action,dateAvailable)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        self.createCarPrint()
        #car type
        carTypeInput = self.__carService.checkCarType()
        make = input("Make (f.x. Toyota Yaris): ").strip().capitalize()
        color = input("Color: ").strip().capitalize()
        passengers = self.__carService.checkPassengers()
        transmissionInput = self.__carService.checkTransmission()
        liecensePlate = self.__carService.checkLicenseplate()
        transmission = self.getTransmission(transmissionInput)
        rentCost, carType = self.getCarTypeVariables(carTypeInput)
        status = 'available'
        rentOutCar, unusedValue = self.getTimeOfOrder()
        returnCar = rentOutCar
        newCar = Car(carType,make,liecensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        print("\nCar successfully created!")
        self.printCarHeader()
        print((str(newCar)))
        self.pressEnterToContinue()
        return newCar


    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

    def getCarTypeVariables(self,carTypeInput):
        if carTypeInput == '1':
            carType = 'Compact'
            rentCost = 14000
        elif carTypeInput == '2':
            carType = 'Comfort'
            rentCost = 20000
        elif carTypeInput == '3':
            carType = 'CUV'
            rentCost = 25000
        elif carTypeInput == '4':
            carType = 'Highland'
            rentCost = 30000
        elif carTypeInput == '5':
            carType = 'Luxury'
            rentCost = 35000
        return rentCost, carType

    '''----------------------------------CAR PRINT FUNCTIONS-----------------------------------------------'''
    def displayAllCarsPrint(self,cars):
        self.printCarHeader()
        for car in cars:
            print((str(car)))

    def findCarTypeMenuPrint(self):
        self.actionsPrint()
        print("0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")
        print("6. Rent out a car")

    def createCarPrint(self):
        self.actionsPrint()
        print("1. Select Compact")
        print("2. Select Comfort")
        print("3. Select CUV")
        print("4. Select Highland")
        print("5. Select Luxury")
    
    def printCarHeader(self):
            LINE = '-'
            print("\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
            'Color', 'Passengers','Transmission','Rent Cost'))
            print("{:-<15} {:-<15} {:-<15} {:-<15} {:-<15} {:-<15} {:-<15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))


    '''----------------------------------ORDER FUNCTIONS-----------------------------------------------'''
    def customerNotFoundMenu(self):
        self.customerNotFoundPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            self.createOrder()
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.customerNotFoundMenu()

    def rentOutToCustomerMenu(self):
        self.rentOutToCustomerPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            return
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.rentOutToCustomerMenu()

    def selectCarType(self):
        self.selectCarTypePrintMenu()
        action = self.__orderService.checkCarTypeSelection()
        rentCost, carType = self.getCarTypeVariables(action)
        return rentCost, carType

    def getCostOfOrder(self, rentOutCarTime, returnCarTime, rentCost):
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days        
        totalCost = int(totalDaysRented) * rentCost
        print("Price for {} days rental is {} ISK without VAT".format(totalDaysRented,totalCost))
        return totalCost, totalDaysRented

    def addInsurance(self, cost):
        insurance = 0
        action = ''
        while action != '1' or action != '2':
            self.addInsurancePrint()
            action = self.chooseAction()
            if action == '1':
                totalCost = cost * 1.05
                insurance = cost * 0.05
                return int(totalCost), int(insurance)
            elif action == '2':
                totalCost = cost
                return int(totalCost), int(insurance)
            else:
                self.invalidAction(action)

    def getTimeOfOrder(self):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minutes = datetime.now().minute
        timeOfOrder = datetime(year, month, day, hour, minutes)
        stringTimeOfOrder = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
        return stringTimeOfOrder, timeOfOrder

    def areYouSure(self):
        self.areYouSurePrint()
        action = self.chooseAction()
        if action == '1':
            return True
        elif action == '2':
            return False
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.areYouSure()

    def finalStepOrder(self, order):
        self.finalStepOrderPrint()
        action = self.chooseAction()
        if action == '1':
            self.__orderService.addOrder(order)
            print("Order complete!")
        elif action == '2':
            status = self.areYouSure()
            if status == True:
                self.mainMenu()
            else:
                self.finalStepOrder(order)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.finalStepOrder(order)

    def createOrder(self):
        #Order Number
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            # find customer
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            print("\nPath: Menu/Create_Car_Order/Customer_Found/\n")
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print((str(customer)))
            self.rentOutToCustomerMenu()
        except:
            print("\nPath: Menu/Create_Car_Order/Customer_Not_Found/")
            self.customerNotFound()
            self.customerNotFoundMenu()
        nothing, orderNumber = self.__orderService.getAllOrders()
        # Time for rental
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
        self.pressEnterToContinue()
        # Choose car type
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/")
        rentCost, carType = self.selectCarType()
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/Add_Insurance/")
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
        # Print out order
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/")
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        # Credit card for insurance
        creditCard = self.creditCardInfo()
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/")
        self.finalStepOrder(order)
        #Choose payment
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/Payment/")
        self.choosePayment(carCost, creditCard)
        # Print receipt
        print("\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/Payment/Receipt/")
        self.showReceipt(order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)

    def displayAllOrders(self, orders):
        print("-------------------------------------------- List of All Orders --------------------------------------------")
        self.displayAllOrdersHeaderPrint()
        for order in orders:
            print(str(order))
            #menu? 

    def returnCarAdditionalPricePrint(self,price):
        print("\nAdditional price to be paid for late delivery: {} ISK\n".format(price))
    
    def returnCarAdditionalPrice(self, returnTimeDifference, searchedCar):
        hourPrice = int(searchedCar.getRentcost())/24*1.25
        hours = returnTimeDifference.seconds / 60 / 60
        price = hours * hourPrice
        self.returnCarAdditionalPricePrint(int(price))
    
    def returnCarPrint(self):
        print("0. Go back")
        print("1. Return a car")
        
    def markCarReturnedPrint(self):
        print("0. Go back")
        print("1. Mark car returned")

    def returnCar(self):
        print("\nPath: Menu/Return_Car/")
        print("\n------------------------------------------------- Return a Car -------------------------------------------------")
        while True:
            self.actionsPrint()
            self.returnCarPrint()
            #ask if sure to return a car
            action = self.chooseAction()
            if action == '0':
                    self.mainMenu()
            elif action == '1':
                licenseplate = self.__carService.checkLicenseplate(False)
                car = self.__carService.licensePlateCheck(licenseplate)
                if car == None:
                    print("\nCar not found!")
                    self.pressEnterToContinue()
                    self.returnCar()
                    return False
                elif car.getStatus() == 'available':
                    print("\nCar is not rented out")
                    self.pressEnterToContinue()
                    self.returnCar()
                    return False
                self.printCarHeader()
                print(str(car))
                self.printReturnMenu()
                action = self.chooseAction()
                if action == '0':
                    self.mainMenu()
                    return False
                elif action == '1':
                    timeOfReturn = self.__orderService.checkValidDate()
                    timeOfreturnInputTimeFormat = self.__orderService.createDate(timeOfReturn)
                    searchedCar = self.__carService.returnCar(licenseplate, timeOfReturn)
                    returnTimeDifference = timeOfreturnInputTimeFormat - searchedCar.getReturnCar()
                    if returnTimeDifference.seconds > 0:
                        self.returnCarAdditionalPrice(returnTimeDifference, searchedCar)
                    print("Car marked returned")
                    return self.pressEnterToContinue()
                else:
                    self.returnCar()
                    return False
            else:
                self.invalidAction(action)

    def rentOutACar(self):
        print("\nPath: Menu/Rent_Out_Car_/Find_Customer\n")
        print("------------------------------------------------ Rent Out a Car ------------------------------------------------\n")
        licensePlate = self.__carService.checkLicenseplate(False)
        searchedCar = self.__carService.licensePlateCheck(licensePlate)
        if searchedCar == None:
            print("\nCar not found!")
            self.rentOutACar()
        # Info about the car to be rented
        print("\nCar found!\n")
        carType = searchedCar.getType()
        make = searchedCar.getMake()
        color = searchedCar.getColor()
        passengers = searchedCar.getPassengers()
        transmission = searchedCar.getTransmission()
        rentCost = searchedCar.getRentcost()
        rentCost = int(rentCost)
        status = searchedCar.getStatus()
        rentOutCar = searchedCar.getRentOutCar() # string format
        returnCar = searchedCar.getReturnCar() # string format
        status = 'unavailable'
        # Prin out the car to be rented
        self.printCarHeader()
        print(str(searchedCar))
        self.pressEnterToContinue()
        #Search for customer for the rental
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print(str(customer))
            self.rentOutToCustomerMenu()
        except:
            self.customerNotFound()
            self.customerNotFoundMenu()
        # Get order number
        nothing, orderNumber = self.__orderService.getAllOrders()
        #Input rent out time and return
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
       # Print out order
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        # Credit card for insurane
        creditCard = self.creditCardInfo()
        self.finalStepOrder(order)
        # edit the car status and rent times
        editedCar = self.__carService.editCar(carType,make,licensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        #Choose payment
        self.choosePayment(carCost, creditCard)
        # Print receipt
        self.showReceipt(order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)

    def choosePaymentPrint(self):
        print("\nChoose payment method")
        self.actionsPrint()
        print("1. Credit card")
        print("2. Cash")

    def choosePayment(self, carCost, creditCard):
        while True:
            self.choosePaymentPrint()
            action = self.chooseAction()
            if action == '1':
                print("Payment will be charged on the following credit card {} for {} ISK".format(creditCard, carCost))
                self.pressEnterToContinue()
                return False
            elif action == '2':
                print("Payment to be paid: {} ISK".format(carCost))
                self.pressEnterToContinue()
                return False
            else:
                action = self.invalidAction(action)
        
    def creditCardInfo(self):
        creditCard = self.__orderService.creditCardInfo()
        return creditCard

    def showReceiptPrint(self):
        print("\nDo you want to get a receipt ?")
        print("1. Yes")
        print("2. No")

    def showReceipt(self, order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
        while True:
            self.showReceiptPrint()
            action = self.chooseAction()
            if action == '1':
                self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)
                self.pressEnterToContinue()
                return False
            elif action == '2':
                self.pressEnterToContinue()
                return False
            else:
                self.invalidAction(action)

    def editOrderInfoMenu(self):
        self.actionsPrint()
        self.lookUpOrderMenuPrint()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            #get order info
            try:
                orderNumber, orderInfo = self.__orderService.checkOrderNumber()#check for illegitimacy##might be stuck in loop
                #prints order info
                #variables for rent cost
                originalRentOutCarTime = self.__orderService.createDate(orderInfo.getStartDate())
                originalReturnCarTime = self.__orderService.createDate(orderInfo.getEndDate())
                originalDaysRented = self.daysRented(originalRentOutCarTime, originalReturnCarTime)
                #NOT THE ORIGINAL PRICE AND 0.0
                originalPrice = orderInfo.getRentCost()
                ##NEEDS FIXING FOR CORRECT INFO IN DISPLAYORDERINFO###
                self.displayOrderInfo(orderInfo, 0, originalDaysRented, originalPrice, originalRentOutCarTime, originalReturnCarTime, orderInfo.getTimeOfOrder())#####
                self.editOrderMenuPrint()
            except:
                self.mainMenu()
            action = self.chooseAction()
            if action == '0':
                self.editOrderInfoMenu()
            elif action == '1':
                #gets beginning of rental time and 
                #edit rental time
                #MISSING RENTOUTTIME OG RENTOUTDATE
                rentOutDate, returnDate, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
                #get type
                newDaysRented = self.daysRented(rentOutCarTime, returnCarTime)
                #get price
                newCostOfRental = int((int(originalPrice) / originalDaysRented) * newDaysRented)
                #new order
                newOrder = self.__orderService.editTimeOfRental(rentOutDate, returnDate, newCostOfRental, orderNumber)
                print("\nRental time updated")
                self.displayAllOrdersHeaderPrint()
                print(str(newOrder))
                self.pressEnterToContinue()

            elif action == '2':
                #Change car type
                rentCost, carType = self.selectCarType()
                newCostOfRental = originalDaysRented * rentCost
                totalCost, insurance = self.addInsurance(newCostOfRental)
                newOrder = self.__orderService.editCarType(totalCost, carType, orderNumber)
                print("Car Type updated")
                self.displayAllOrdersHeaderPrint()
                print(str(newOrder))
                self.pressEnterToContinue()
            
            elif action == '3':
                #Cancel order
                confirmingCancellation = self.areYouSure()
                if confirmingCancellation == True:
                    deletedOrder = self.__orderService.cancelOrder(orderNumber)
                    print("\nOrder number: {} deleted".format(orderNumber))
                    self.displayAllOrdersHeaderPrint()
                    print(str(deletedOrder))
                    self.pressEnterToContinue()
            else:
                self.editOrderInfoMenu()
        else:
            self.editOrderInfoMenu()

    def daysRented(self, rentOutCarTime, returnCarTime):
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days

        return int(totalDaysRented)


    def editOrderMenuPrint(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Edit rental time")
        print("2. Change car type")
        print("3. Cancel order")

    
    def lookUpOrderMenuPrint(self):
        print("--------------------------------------------Look Up an Order--------------------------------------------")
        print("0. Go back")
        print("1. Search for order")


    

    '''--------------------------ORDER PRINT FUNCTIONS--------------------------'''
    def rentOutToCustomerPrintMenu(self):
        self.actionsPrint()
        print("0. Go back to main menu")
        print("1. Select customer")

    def customerNotFoundPrintMenu(self):
        self.actionsPrint()
        print("0. Go back to main menu")
        print("1. Search again")

    def selectCarTypePrintMenu(self):
        self.actionsPrint()
        print("1. Compact")
        print("2. Comfort")
        print("3. CUV")
        print("4. Highland")
        print("5. Luxury")

    def addInsurancePrint(self):
        self.actionsPrint()
        print("1. Add SCDW:\n{0}:\n\t{1}\n\t{2}\n\t{3}\n\t{4}".format("Includes","-Front window","-Sandstorm","-Chassis", "-Theft insurance"))
        print("2. No additional insurance")

    def areYouSurePrint(self):
        print("\nAre you sure you want to cancel?")
        print("1. Yes")
        print("2. No, go back")

    def finalStepOrderPrint(self):
        self.actionsPrint()
        print("1. Save and complete order")
        print("2. Cancel order")

    def displayAllOrdersHeaderPrint(self):
        LINE = '-'
        print("\n{:13} {:20} {:12} {:10} {:18} {:18} {:18} {:10}".format('Order number', 'Customer', 'SSN', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:-<13} {:-<20} {:-<12} {:-<10} {:-<18} {:-<18} {:-<18} {:-<12}".format(LINE,LINE, LINE, LINE, LINE, LINE, LINE, LINE))

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
# THIS LOOKS HORRIBLE, FIX LATER
        LINE = '-'
        print("\n-------------------------------------------------- Order Info --------------------------------------------------\n")
        # print("Order Number: {}\n".format(order.getOrderNumber()))
        print("Order number: ",str(order.getOrderNumber()))
        print("\n{:20} {:20}".format('Name','SSN'))
        print("{:-<32}".format(LINE))
        print("{:20} {:20}".format(order.getCustomer(), order.getSsn()))
        print("\n{:10} {:20} {:20} {:20}".format('Car type','From','To','Date rented'))
        print("{:-<10} {:-<20} {:-<20} {:-<20}".format(LINE,LINE,LINE,LINE))
        print("{:10} {:20} {:20} {:20}".format(order.getCarType(),str(rentOutCarTime),str(returnCarTime), str(timeOfOrder)))
        print("\nCost of",str(totalDaysRented),"days without VAT: ",str(carCost),"ISK")
        if insurance != 0:
            print("Extra insurance: ",str(insurance),"ISK")
            # print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))
            print("\nTotal cost of",str(totalDaysRented),"days without VAT: ",str(order.getRentCost())," ISK")

    def searchCustomerForCarRentalHeaderPrint(self):
        print("\n------------------------------------------Find Customer for Car Rental ------------------------------------------")

    def printReturnMenu(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Return selected car")
    ##NOT IN USE###
    def listofOrdersMenu(self):
        self.actionsPrint()
        print("0. Go back")
        print("1. Search for an order by order number")
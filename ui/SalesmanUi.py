from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer


class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()

    def mainMenu(self):
        action = ''
        while action != 'q':
            self.mainMenuPrint()
            action = input('Action: ')

            if action == '1' or action == '2':
                typeAction = ''
                cars = self.__carService.getCars(action, typeAction)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action)


            elif action == '3':
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)

            elif action == '5':
                self.findCustomerMenu()

            elif action == '10':
                carType,make,licenseplate,color,passengers,transmission,rentCost,status = self.createCar()
                newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status)
                self.__carService.addCar(newCar)

            elif action == 'q':
                print("Exiting program..")
                exit()

            else:
                print("Invalid action")
                self.mainMenu()


    def mainMenuPrint(self):
        print("\nYou can do the following: ")
        print("1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Register customer.")
        print("4.  Create car reservation.")
        print("5.  Find a customer.")
        print("6.  Look up an order.")
        print("7.  Show list of orders.")
        print("8.  Return a car.")
        print("9.  Edit order.")
        print("10. Register car")
        print("press q to quit\n")




    ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.findCustomerMenuPrint()
        findCustomerAction = input("Choose action: ")
    #Going to menu
        if findCustomerAction == '0':
            self.mainMenu()
    #Finding customer
        elif findCustomerAction == '1':
            self.searchCustomerHeaderPrint()
            searchTerm = input("Input SSN or Customernumber to find: ")
            customer = self.__customerService.findCustomer(searchTerm)
            if customer == None:
                print()
                print("Customer not found!")
                self.findCustomerMenu()
            else:
                self.displayCustomerHeaderPrint() #This displays the customer
                print(customer)
                self.afterCustomerIsFoundPrint()
                self.afterCustomerIsFoundMenu(customer)
    #show all customers
        elif findCustomerAction == '2':
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            self.findCustomerMenu()


    def afterCustomerIsFoundPrint(self):
        print("\nActions:\n")
        print("0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer")

    def afterCustomerIsFoundMenu(self, customer):
        afterCustomerFoundAction = input("Choose action: ")
        if afterCustomerFoundAction == '0':
            self.findCustomerMenu()
        elif afterCustomerFoundAction == '1':
            self.editCustomerInfo(customer)
        elif afterCustomerFoundAction == '2':
            self.warningMessagePrint(customer)
            self.warningMessageMenu(customer)
    
    def editCustomerInfoMenu(self):
            print("1. Edit customer name")
            print("2. Edit customer age")
            print("3. Edit customer SSN")
            print("4. Edit customer address")
            print("5. Edit All customer information")
            
# The menu for editing the customer information, Number stays the same
    def editCustomerInfo(self,customer):
            self.editCustomerInfoMenu()
            cs = CustomerService()
            afterEditCustomerSelectedAction = input("Choose action: ")
        # Edit customer name
            if afterEditCustomerSelectedAction =='1':
                name = cs.inputNameCheck()
                age = customer.getAge()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer age
            if afterEditCustomerSelectedAction =='2':
                name = customer.getName()
                age = cs.inputAgeCheck()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer ssn
            if afterEditCustomerSelectedAction =='3':
                name = customer.getName()
                age = customer.getAge()
                ssn = cs.inputSsnCheck()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer address
            if afterEditCustomerSelectedAction =='4':
                
                name = customer.getName()
                age = age = customer.getAge()
                ssn = customer.getSsn()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)


        #Edit all customer information
            if afterEditCustomerSelectedAction == '5':
                cs = CustomerService()
                name = cs.inputNameCheck()
                age = cs.inputAgeCheck()
                ssn = cs.inputSsnCheck()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)


    def warningMessagePrint(self,customer):
        print("\n")
        print("Warning: Are you sure you want to delete this customer?")
        print(customer)
        print("\n")
        print("1. Yes, delete this customer")
        print("2. No, do not deleted this customer")

    def warningMessageMenu(self,customer):
        warningMessageAction = input("Choose action")
        while warningMessageAction:
            if warningMessageAction == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                self.afterCustomerIsFoundMenu(customer)
            elif warningMessageAction == '2':
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.warningMessageMenu(customer)
        

    def createCustomer(self):
        print("-----------Creating customer account-----------")
        cs = CustomerService()
        name = cs.inputNameCheck()
        age = cs.inputAgeCheck()
        ssn = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.getSumOfAllCustomers()
    
        return name,age,ssn,address,number

    # Displays options that the user has.
    def findCustomerMenuPrint(self):
        print("\n0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")

    def displayCustomerHeaderPrint(self):
        print("\n")
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "---------------", "---------------"))

    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)
    
    
    def searchCustomerHeaderPrint(self):
        print("--------------------------------------------Search for customer-------------------------------------------")


    
    
    
    ''' -------------------- Car Functions -------------------- '''

    def findCarTypeMenuPrint(self):
        print("0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")

    def showCarsByTypeMenu(self, action):
        while True:
            self.findCarTypeMenuPrint()
            typeAction = input('Choose action: ')
            if typeAction == '0':
                break
            elif typeAction == '1':
                typeAction = 'compact'
            elif typeAction == '2':
                typeAction = 'comfort'
            elif typeAction == '3':
                typeAction = 'CUV'
            elif typeAction == '4':
                typeAction = 'highland'
            elif typeAction == '5':
                typeAction = 'luxury'
            cars = self.__carService.getCars(action, typeAction)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        print("\nSelect from Car Types:\n1. Compact\n2. Comfort\n3. CUV\
                \n4. Highland\n5. Luxury\n")
        while True:
            try:
                carTypeInput = int(input('Choose car type number:  '))
                if 0 < carTypeInput < 6:
                    break
                else:
                    print('Please choose from available types\n')
            except:
                print("Please only insert integer values\n")
        make = input('Make (f.x. Toyota Yaris): ').capitalize()
        color = input('Color: ').capitalize()
        while True:
            try:
                passengers = int(input('Passengers: '))
                break
            except:
                print("\nPlease only insert integer values\n")
        print("Transmission:\n1. Auto\n2. Manual\n")
        while True:
            try:
                transmissionInput = int(input('Choose: '))
                if 0 < transmissionInput < 3:
                    break
                else:
                    print('Please choose from available transmissions\n')
            except:
                print("Please only insert integer values\n")
        transmission = self.getTransmission(transmissionInput)
        while True:
            licenseplate = input('License plate (F.x. LL-L00): ').upper()
            if len(list(licenseplate)) == 6:
                break
            else:
                print("Not a valid license plate")

        rentCost, carType = self.findRentCost(carTypeInput)
        status = 'available'
        newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status)
        print("\nCar successfully created!")
        self.printCarHeader()
        print(newCar)
        return carType,make,licenseplate,color,passengers,transmission,rentCost,status

    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

    def findRentCost(self,carTypeInput):
        if carTypeInput == 1:
            carType = 'Compact'
            rentCost = 14000
        if carTypeInput == 2:
            carType = 'Comfort'
            rentCost = 20000
        if carTypeInput == 3:
            carType = 'CUV'
            rentCost = 25000
        if carTypeInput == 4:
            carType = 'Highland'
            rentCost = 30000
        if carTypeInput == 5:
            carType = 'Luxury'
            rentCost = 35000
        return rentCost, carType

    def displayAllCarsPrint(self,cars):
        self.printCarHeader()
        for car in cars:
            print(car)

    def printCarHeader(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))

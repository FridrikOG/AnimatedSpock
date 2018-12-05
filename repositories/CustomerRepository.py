from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []
        self.__setCustomers = set()
        self.__ssnCustomers = set()

    def addCustomer(self,customer):
        with open('./data/customers.csv','a',) as customerFile:
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            address = customer.getAddress()
            number = customer.getNumber()
            customerFile.write(f'{name},{age},{ssn},{address}, {number}\n')

    def getAllCustomers(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    name = line['name']
                    age = line['age']
                    ssn = line['ssn']
                    address = line['address']
                    number = line['number']
                    newCustomer = Customer(name, age, ssn, address, number)
                    self.__customers.append(newCustomer)

                    # if ssn not in self.__ssnCustomers:
                    #     newCustomer = name +'   '+ age+'    ' + ssn
                    #     self.__ssnCustomers.add(newCustomer)   
        return self.__customers

    def findCustomer(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                if line not in self.__setCustomers:
                    self.__setCustomers.add(line)
        return self.__setCustomers
        
        


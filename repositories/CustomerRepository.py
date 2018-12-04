from models.Customer import Customer

class CustomerRepository:
    def __init__(self):
        self.__customers = []

    def addCustomer(self,customer):
        # with open('./data/customers.txt','a') as customerFile:
        #     name = customer.getName()
        #     age = customer.getAge()
        #     ssn = customer.getSsn()
        #     customerFile.write(f'{name},{age},{ssn}\n')
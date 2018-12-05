class Customer():
    def __init__(self,name,age,ssn):
        self.__name = name
        self.__age = age
        self.__ssn = ssn

    def __str__(self):
        s = f'Name: {self.__name}\n'
        s += f'Age: {self.__age}\n'
        s += f'SSN: {self.__ssn}\n'
        return s
    
    def __repr__(self):
        return self.__str__()

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age
    
    def getSsn(self):
        return self.__ssn
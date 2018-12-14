from repositories.OrderRepository import OrderRepository
from datetime import datetime, timedelta
from models.Colors import Colors

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()
        

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------

    def addOrder(self, order):
        self.__orderRepo.addOrder(order)

    def creditCardInfo(self):
        while True:
            try:
                print("\nInsert credit card information for insurance in this format XXXX-XXXX-XXXX-XXXX")
                creditCard = input("Credit card: ").strip()
                if len(creditCard) == 19:
                    creditList = creditCard.split('-')
                    for split in creditList:
                        if len(split) == 4:
                            int(creditList[0])
                            int(creditList[1])
                            int(creditList[2])
                            int(creditList[3])
                            return creditCard
                        else:
                            self.insertValidCardPrint()
                else:
                    self.insertValidCardPrint()
            except:
                self.insertValidCardPrint()

    def insertValidCardPrint(self):
        print("\nPlease insert a valid credit card")


    def createDate(self, rentDate):
        day, month, year, hour, minutes = map(int, rentDate.split('-'))
        return datetime(year, month, day, hour, minutes)

    def checkValidDate(self, newOrder=False):#SEGJA AÐ SÉ SATT FYRIR NEW ORDER

        if newOrder == True:
            while True:
                print("\nInput time of rental:")
                rentOutCar = self.InputValidDate()
                rentOutCarTime = self.getTime(rentOutCar)
                if rentOutCarTime > datetime.now():
                    break
                else: 
                    print('\nPlease insert valid start of rental time\n')
                    
            while True:
                print("\nInput time of return:")
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime > rentOutCarTime:
                    return rentOutCar, returnCar, rentOutCarTime, returnCarTime
                else:
                    print('Please insert valid end of rental time')
        #ef ekki ný pöntun
        else:
            while True:
                print("\nInput time of return:")
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime.day == datetime.now().day and returnCarTime.month == datetime.now().month:
                    break
                else:
                    print("Please insert valid end of rental time")
            return returnCar

    def checkOrderNumber(self):
        numberExists = True
        while numberExists:
            try:
                orderNumber = input("Enter Order number: ").strip()
                intOrder = int(orderNumber)
                if numberExists == self.__orderRepo.checkOrderNumber(orderNumber):
                    orderInfo = self.__orderRepo.findOrder(orderNumber)
                    return orderNumber, orderInfo
                else:
                    print("Order number does not exist")
            except:
                print("Order number does not exist")
                print("\n""Actions: ")
                print("0. Go back to main menu")
                print("1. Input order number again")
                action = input("\nChoose action: ").strip()
                if action == '0':
                    break 
                elif action == '1':
                    pass

    def editTimeOfRental(self, startOfRental, endOfRental, rentCost, orderNumber):
        #     #edit order
        updatedOrder = self.__orderRepo.editOrderVariable('1', orderNumber, startOfRental, endOfRental, rentCost)
        return updatedOrder

    def editCarType(self, totalCost, carType, orderNumber):
        updatedCar = self.__orderRepo.editOrderVariable('2', orderNumber, totalCost, carType)
        return updatedCar

    def cancelOrder(self, orderNumber):
        canceledOrder = self.__orderRepo.editOrderVariable('3', orderNumber)
        return canceledOrder


    def getTime(self, date):
        try:
            day, month, year, hour, minutes = map(int, date.split('-'))
            return datetime(year, month, day, hour, minutes)
        except ValueError:
            print("Not a valid time")
            return datetime(1,1,1)

    def InputValidDate(self):
        while True:
            try:
                dateInput = input('1/2 - Input date in this format DD-MM-YYYY: ').strip()
                timeInput = input('2/2 - Input time in this format HH:MM: ').strip()
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
                break
            except:
                print("\nplease input a valid date\n")
        return finalDateTime

    def checkCarTypeSelection(self):
        while True:
            try:
                action = input("\nSelect car type for rental: ").strip()
                checkint = int(action)
                if '1' <= action <= '5':
                    return action
                else:
                    print("\nPlease choose from available options")


            except:
                print("\nPlease choose from available options")



    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)
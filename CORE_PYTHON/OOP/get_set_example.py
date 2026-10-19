#1
class MovieTicket:
    def __init__(self,ticketNo1,moviename1,price1):
        self.ticketNo=ticketNo1
        self.moviename=moviename1
        self.price=price1

    def get_ticketNo(self):
        return self.ticketNo
    def set_ticketNo(self,newticketNo):
        self.ticketNo=newticketNo

    def getMovieName(self):
        return self.moviename
    def setMovieName(self,newname):
        self.moviename=newname

    def get_Price(self):
        return self.price
    def set_Price(self,newprice):
        self.price=newprice

    def display(self):
        print(f'TicketNo={self.ticketNo}\tMovie={self.moviename}\tPrice={self.price}')


m1=MovieTicket(501,'Dhurandhar',250)
m1.display()
m1.set_Price(300)
m1.display()

#2-------------------------------------------------------------------------------------------------
'''class ATM:
    def __init__(self,cardNo,balance,pin):
        self.cardno=cardNo
        self.balance=balance
        self.pin=pin

    def getcardNo(self):
        return self.cardno
    def setcardNo(self,newcardNo):
        self.cardNo=newcardNo
    def getBalance(self):
        return self.balance
    def setBalance(self,newbalance):
        self.balance=newbalance

    def getPin(self):
        return self.pin
    def setPin(self,newpin):
        self.pin=newpin

    def display(self):
        print(f'CardNo={self.cardno}\tBalance={self.balance}\tPIN={self.pin}')


a1=ATM(45678,9000000,7020)
a1.display()
a1.setBalance(1000000)
a1.display()
'''
#3---------------------------------------------------------------------------------------------------
'''class RailwayTicket:
    def __init__(self,ticketNo,passenger,seatno):
        self.ticketNo=ticketNo
        self.passenger=passenger
        self.seatno=seatno

    def get_ticketNo(self):
        return self.ticketNo
    def set_ticketNo(self,newticketNo):
        self.ticketNo=newticketNo

    def getPassenger(self):
        return self.passenger
    def setPassenger(self,newpassenger):
        self.passenger=newpassenger

    def getSeatno(self):
        return self.seatno
    def setSeatno(self,newseatno):
        self.seatno=newseatno

    def display(self):
        print(f'TicketNo={self.ticketNo}\tPassenger={self.passenger}\tSeatNo={self.seatno}')


r1=RailwayTicket(1001,'Ganesh',25)
r2=RailwayTicket(1002,'vishal',35)
r1.display()
r2.display()
r1.setSeatno(30)
r1.display()
r2.setSeatno(31)
r2.display()
'''
#4---------------------------------------------------------------------------------------------------
'''class BankAccount:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance

    def getAccno(self):
        return self.accno
    def setAccno(self, newaccno):
        self.accno = newaccno

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance
    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f'AccNo={self.accno}\tName={self.name}\tBalance={self.balance}')


b1 = BankAccount(1001, 'Ganesh', 70000)
b2 = BankAccount(1002, 'Vishal', 45000)

print(b1.getName())
b1.display()
b2.display()
b2.setBalance(75000)
b2.display()'''

#5---------------------------------------------------------------------------
'''class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f'Id={self.id}\tName={self.name}\tPrice={self.price}')


p1 = Product(101, 'TV', 55000)
p2 = Product(102, 'Mobile', 25000)
p1.display()
p2.display()
p2.setPrice(22000)
p2.display()'''
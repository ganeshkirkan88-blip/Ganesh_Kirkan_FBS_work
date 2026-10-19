'''#1-------------------------------------------------------------
class person:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

# person ends heae....

class Nurse(person):
    def __init__(self, id1, name1, sal1, com1):
        super().__init__(id1, name1, sal1)
        self.com = com1

    def getCom(self):
        return self.com

    def setCom(self, newcom):
        self.com = newcom

    def display(self):
        print(f"Com={self.com}")
        return super().display()

# class doctor ends here....

class Doctor(person):
    def __init__(self, id1, name1, sal1,bonus):
        super().__init__(id1, name1, sal1)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, newbonus):
        self.bonus = newbonus

    def display(self):
        print(f"Bonus={self.bonus}")
        return super().display()    
# class Developer ends here....

p1 = person(10, "Sachin", 121214)
n1 = Nurse(11, "Virat", 33424,5000)
d1 = Doctor(12, "Rohit", 8965,15000)
p1.display()
n1.display()
d1.display()'''

#2-------------------------------------------------------------
'''class Police:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

# person ends heae....

class Inspector(Police):
    def __init__(self, id1, name1, sal1, com1):
        super().__init__(id1, name1, sal1)
        self.com = com1

    def getCom(self):
        return self.com

    def setCom(self, newcom):
        self.com = newcom

    def display(self):
        print(f"Com={self.com}")
        return super().display()

# class doctor ends here....

class Constable(Police):
    def __init__(self, id1, name1, sal1,Area):
        super().__init__(id1, name1, sal1)
        self.Area = Area

    def getBonus(self):
        return self.Area

    def setBonus(self, newArea):
        self.Area = newArea

    def display(self):
        print(f"Area={self.Area}")
        return super().display()    
# class Developer ends here....

p1 = Police(10, "Sachin", 121214)
i1 = Inspector(11, "Virat", 45000,70000)
c1 = Constable(12, "Rohit", 13000,'pune')
p1.display()
i1.display()
c1.display()'''

#3--------------------------------------------------------------------------------
class BankPerson:
    def __init__(self, id1, name1, mobile1):
        self.id = id1
        self.name = name1
        self.mobile = mobile1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getMobile(self):
        return self.mobile

    def setMobile(self, newmobile):
        self.mobile = newmobile

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tMobile={self.mobile}")

# class bank_person ends here................

class Customer(BankPerson):
    def __init__(self, id1, name1, mobile1, balance1):
        super().__init__(id1, name1, mobile1)
        self.balance = balance1

    def getBalance(self):
        return self.balance

    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Balance={self.balance}")
        return super().display()
#class customer ends here.............................................................

class Manager(BankPerson):
    def __init__(self, id1, name1, mobile1, branch1):
        super().__init__(id1, name1, mobile1)
        self.branch = branch1

    def getBranch(self):
        return self.branch

    def setBranch(self, newbranch):
        self.branch = newbranch

    def display(self):
        print(f"Branch={self.branch}")
        return super().display()
    
#class manager ends here........................

b1 = BankPerson(1, "Shree", "9354673372")
c1 = Customer(2, "Ganesh", "7020962851", 75000)
m1 = Manager(3, "vishal", "3546728767", "Pimpri")

b1.display()
c1.display()
m1.display()

#4-----------------------------------------------------------------------

class RailwayPerson:
    def __init__(self, id1, name1, age1):
        self.id = id1
        self.name = name1
        self.age = age1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age

    def setAge(self, newage):
        self.age = newage

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tAge={self.age}")

# calss Railwayperson ends here..................


class Passenger(RailwayPerson):
    def __init__(self, id1, name1, age1, seat1):
        super().__init__(id1, name1, age1)
        self.seat = seat1

    def getSeat(self):
        return self.seat

    def setSeat(self, newseat):
        self.seat = newseat

    def display(self):
        print(f"Seat={self.seat}")
        return super().display()

#class passenger ends here......................................

class TC(RailwayPerson):
    def __init__(self, id1, name1, age1, train1):
        super().__init__(id1, name1, age1)
        self.train = train1

    def getTrain(self):
        return self.train

    def setTrain(self, newtrain):
        self.train = newtrain

    def display(self):
        print(f"Train={self.train}")
        return super().display()

#class TC ends here.....................


r1 = RailwayPerson(1, "Raj", 40)
p1 = Passenger(2, "Amit", 25, "B2-45")
t1 = TC(3, "Suresh", 38, "kachikuda Express")

r1.display()
p1.display()
t1.display()

#5---------------------------------------------------------------------------------------------
class Sportsperson:
    def __init__(self, id1, name1, age1):
        self.id = id1
        self.name = name1
        self.age = age1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age

    def setAge(self, newage):
        self.age = newage

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tAge={self.age}")

# class sportsperson ends here................................


class Cricketer(Sportsperson):
    def __init__(self, id1, name1, age1, runs1):
        super().__init__(id1, name1, age1)
        self.runs = runs1

    def getRuns(self):
        return self.runs

    def setRuns(self, newruns):
        self.runs = newruns

    def display(self):
        print(f"Runs={self.runs}")
        return super().display()

#class cricketer ends here..............................


class Footballer(Sportsperson):
    def __init__(self, id1, name1, age1, goals1):
        super().__init__(id1, name1, age1)
        self.goals = goals1

    def getGoals(self):
        return self.goals

    def setGoals(self, newgoals):
        self.goals = newgoals

    def display(self):
        print(f"Goals={self.goals}")
        return super().display()

#class footballer ends here..............................

s1 = Sportsperson(1, "Vishal", 37)
c1 = Cricketer(2, "Virat", 39, 11000)
f1 = Footballer(3, "Nagesh", 40, 95)

s1.display()
c1.display()
f1.display()
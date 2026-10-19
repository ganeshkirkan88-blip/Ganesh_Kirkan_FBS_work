#1-------------------------------------------------------
class Police:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
            return self.id
    def setId(self,newid):
            self.id=newid
    
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
    
    def getsal(self):
            return self.sal
    def setsal(self,newsal):
            self.sal=newsal

    def calsal(self):
        print(f'Final salary of Police {self.sal}')


class Inspector(Police):
    def __init__(self, id, name, sal, allowance):
        super().__init__(id, name, sal)
        self.allowance = allowance

    def getallowance(self):
            return self.allowance
    def setallowance(self,newallowance):
            self.allowance=newallowance
    

    def calsal(self):
        print(f'Final salary of Inspector {self.sal + self.allowance}')


class Constable(Police):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
                return self.Bonus
        def setBonus(self,newBonus):
                self.Bonus=newBonus

    def calsal(self):
        print(f'Final salary of Constable {self.sal + self.bonus}')


p1 = Police(1, 'Ganesh', 30000)
i1 = Inspector(2, 'Vikas', 50000, 10000)
c1 = Constable(3, 'Shubham', 25000, 5000)

p1.calsal()
i1.calsal()
c1.calsal()

#2------------------------------------------------------------------------------
class Staff:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
            return self.id
    def setId(self,newid):
            self.id=newid
        
    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname
        
    def getsal(self):
            return self.sal
    def setsal(self,newsal):
            self.sal=newsal

    def calsal(self):
        print(f'Final salary of Staff {self.sal}')


class Teacher(Staff):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def calsal(self):
        print(f'Final salary of Teacher {self.sal + self.bonus}')


class Principal(Staff):
    def __init__(self, id, name, sal, allowance):
        super().__init__(id, name, sal)
        self.allowance = allowance

    def calsal(self):
        print(f'Final salary of Principal {self.sal + self.allowance}')


s1 = Staff(1, 'Amit', 20000)
t1 = Teacher(2, 'Rahul', 40000, 5000)
p1 = Principal(3, 'Rajesh', 80000, 15000)

s1.calsal()
t1.calsal()
p1.calsal()

#3-----------------------------------------------------------
class Hospital:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def calsal(self):
        print(f'Salary of Hospital Staff {self.sal}')


class Doctor(Hospital):
    def __init__(self, id, name, sal, fees):
        super().__init__(id, name, sal)
        self.fees = fees

    def calsal(self):
        print(f'Salary of Doctor {self.sal + self.fees}')


class Nurse(Hospital):
    def __init__(self, id, name, sal, allowance):
        super().__init__(id, name, sal)
        self.allowance = allowance

    def calsal(self):
        print(f'Salary of Nurse {self.sal + self.allowance}')


h1 = Hospital(1, 'Amit', 20000)
d1 = Doctor(2, 'Vikas', 80000, 10000)
n1 = Nurse(3, 'Priya', 30000, 5000)

h1.calsal()
d1.calsal()
n1.calsal()

#4---------------------------------------------------------------------------
class Transport:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def calsal(self):
        print(f'Salary of Transport Staff {self.sal}')


class Driver(Transport):
    def __init__(self, id, name, sal, overtime):
        super().__init__(id, name, sal)
        self.overtime = overtime

    def calsal(self):
        print(f'Salary of Driver {self.sal + self.overtime}')


class Conductor(Transport):
    def __init__(self, id, name, sal, allowance):
        super().__init__(id, name, sal)
        self.allowance = allowance

    def calsal(self):
        print(f'Salary of Conductor {self.sal + self.allowance}')


t1 = Transport(1, 'Ganesh', 20000)
d1 = Driver(2, 'Vikas', 30000, 5000)
c1 = Conductor(3, 'Shubham', 25000, 3000)

t1.calsal()
d1.calsal()
c1.calsal()

#5-------------------------------------------------------------------------------
class School:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def calcFees(self):
        print(f'School Fees = {self.fees}')


class Primary(School):
    def __init__(self, name, fees, books):
        super().__init__(name, fees)
        self.books = books

    def calcFees(self):
        print(f'Primary Fees = {self.fees + self.books}')


class Secondary(School):
    def __init__(self, name, fees, lab):
        super().__init__(name, fees)
        self.lab = lab

    def calcFees(self):
        print(f'Secondary Fees = {self.fees + self.lab}')


s1 = School('PN School', 10000)
p1 = Primary('Primary', 12000, 2000)
s2 = Secondary('Secondary', 20000, 5000)

s1.calcFees()
p1.calcFees()
s2.calcFees()
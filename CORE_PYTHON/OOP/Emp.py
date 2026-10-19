#
'''class Employee:
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal = newsal

    def display(self):
        print(f'Id={self.id}\t Name={self.name}\t Sal={self.sal}')
        
#Employee class ends here.....................................

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcommi(self):
        return self.com
    def setcom(self,newcom):
        self.com=newcom
    def display(self):
        print(f'Com={self.com}')
        return super().display()

#class Hr ends here............................

class Devloper(Employee):
    def __init__(self,id,name,sal,Bonus):
        super().__init__(id,name,sal)
        self.Bonus=Bonus
    def getBonus(self):
        return self.Bonus
    def setBonus(self,newBonus):
        self.Bonus=newBonus

    def display(self):
        print(f'Bonus={self.Bonus}')
        return super().display()

#class Devloper ends here.........
e1=Employee(11,'ganesh',70000)
h1=Hr(12,'Vikas',150000,25000)
d1=Devloper(13,'shubham',250000,50000)
e1.display()
h1.display()
d1.display()'''

#polymorphism-------------------------------------------------
'''class Employee:
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1
    def getId(self):
        return self.id
    def setId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal = newsal

    def calsal(self):
        print(f'Final salary of employee{self.sal}')

    def display(self):
        print(f'Id={self.id}\t Name={self.name}\t Sal={self.sal}')
        
#Employee class ends here.....................................

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcommi(self):
        return self.com
    def setcom(self,newcom):
        self.com=newcom

    def calsal(self):
        print(f'Final salary of Hr{self.sal + self.com}')
    def display(self):
        print(f'Com={self.com}')
        return super().display()

#class Hr ends here............................

class Devloper(Employee):
    def __init__(self,id,name,sal,Bonus):
        super().__init__(id,name,sal)
        self.Bonus=Bonus
    def getBonus(self):
        return self.Bonus
    def setBonus(self,newBonus):
        self.Bonus=newBonus

    def calsal(self):
        print(f'Final salary of Devloper{self.sal + self.Bonus}')

    def display(self):
        print(f'Bonus={self.Bonus}')
        return super().display()

#class Devloper ends here.........
e1=Employee(11,'ganesh',70000)
h1=Hr(12,'Vikas',150000,25000)
d1=Devloper(13,'shubham',250000,50000)
e1.calsal()
h1.calsal()
d1.calsal()'''

# Inheritance-----------------------------------------
class Student:
    stCount=0
    def __init__(self, frn, name, bname):
        self.frn=frn
        self.name=name
        self.batch=bname
        Student.stCount+=1
    def display(self):
        print(f"FRN={self.frn}\tName={self.name} \t Batch={self.batch} \tStudent Count={Student.stCount}")

#student ends here..........
#super :- It is a special type of function which is use to access everything present in a base calss.
#         It is use for constractor change.
class placedStudent(Student):
    def __init__(self, frn, name, bname, cName):
        super().__init__(frn,name,bname)
        self.cName=cName
    def setcName(self,cName):
        self.cName=cName
    def getcName(self):
        return self.cName
    def display(self):
        print(f"cName={self.cName}")
        super().display()

s1=Student(12,"GAurav","April")
s2=Student(1,"Atharva","Jul/aug")
s3=Student(53,"Rutika","Jul/aug")
s4=placedStudent(37,"Shivaraj","Jul/aug","TCS")
s5=placedStudent(18,"Virat","Jul/aug","One8")
print(Student.stCount)


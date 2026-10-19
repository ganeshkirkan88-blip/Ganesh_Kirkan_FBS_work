#1--------------------------------------------------------------------
'''class Student:
    def __init__(self,frnNo,name,batch,iname):
        self.frnNo=frnNo
        self.name=name
        self.batch=batch
        self.iname=iname

    def get_FrnNo(self):
        return self.frnNo
    def set_FrnNo(self,newfrnNo):
        self.frnNo=newfrnNo

    def get_name(self):
        return self.name
    def set_name(self,newname):
        self.name=newname

    def get_batch(self):
        return self.batch
    def set_batch(self,newbatch):
        self.batch=newbatch

    def get_iname(self):
            return self.iname
    def set_iname(self,newiname):
            self.iname=newiname
       
    def display(self):
        print(f'FRN_No={self.frnNo}\tName={self.name}\tBatch={self.batch}')
s1=Student(12,'Gaurav','17April','FBS')
s2=Student(22,'Suraj','Aug','FBS')
s3=Student(17,'Pramod','jul/Aug','FBS')
s1.display()
s2.display()
s3.display()
'''
#2----------------------------------------------------------------
'''class Student:
    stCount = 0
    def __init__(self, frn, name, bname):
        self.frn=frn
        self.name=name
        self.batch=bname
        Student.stCount+=1

    def get_Frn(self):
        return self.frn
    def set_Frn(self,newfrn):
        self.frn=newfrn
    
    def get_name(self):
        return self.name
    def set_name(self,newname):
        self.name=newname
    
    def get_bname(self):
        return self.bname
    def set_bname(self,newbname):
        self.bname=newbname
    
        
    def display(self):
        print(f"FRN={self.frn}\tName={self.name} \t Batch={self.batch} \tStudent Count={Student.stCount}")

class placedStudent:
    def __init__(self, frn, name, bname, cName):
        self.frn=frn
        self.name=name
        self.batch=bname
        self.cName=cName
    def display(self):
        print(f"FRN={self.frn}\tName={self.name} \t Batch={self.batch} \tCName={self.cName}")

s1=Student(12,"GAurav","April")
s2=Student(1,"Atharva","Jul/aug")
s3=Student(53,"Rutika","Jul/aug")
s4=placedStudent(37,"Shivaraj","Jul/aug","TCS")
s5=placedStudent(18,"Viart","Jul/aug","One8")
print(Student.stCount)'''

#3 Inheritance Example ------------------------------------------------------------------------------------
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

#4------------------------------------------------------------------------------
'''class Employee():
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

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

    
    def display(self):
        print(f'Id={self.id}\tName={self.name}\tSal={self.sal}')

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


#polimorphism  Example :- 
'''class Employee():
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

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
        print(f'Final salary of Employee{self.sal}')

    def display(self):
        print(f'Id={self.id}\tName={self.name}\tSal={self.sal}')

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcom(self):
        return self.com
    def setcom(self,newcom):
        self.com=newcom

    def calsal(self):
        print(f'Final salary of Hr {self.sal + self.com}')

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
        print(f'final salary of Devloper {self.sal + self.Bonus}')

    def display(self):
        print(f'Bonus={self.Bonus}')
        return super().display()

#class Devloper ends here.........
e1=Employee(11,'ganesh',70000)
h1=Hr(12,'Vikas',150000,25000)
d1=Devloper(13,'shubham',250000,50000)
e1.calsal()
h1.calsal()
d1.calsal()
'''
#_str_method Example
'''from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self, id1, name1, fees1):
        self.id = id1
        self.name = name1
        self.fees = fees1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.nam
    def setName(self, newname):
        self.name = newname

    def getFees(self):
        return self.fees
    def setFees(self, newfees):
        self.fees = newfees

    @abstractmethod
    def calFees(self):
        pass

    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tFees={self.fees}"

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tFees={self.fees}")


class EngineeringStudent(Student):
    def __init__(self, id1, name1, fees1, labfees):
        super().__init__(id1, name1, fees1)
        self.labfees = labfees

    def calfees(self):
        print(f"Final fees of Engineering={self.fees + self.labfees}")

    def __str__(self):
        return super().__str__() + f"\tLab Fees={self.labfees}"
    
    def display(self):
        print(f"Lab Fees={self.labfees}")
        super().display()


class MedicalStudent(Student):
    def __init__(self, id1, name1, fees1, practicalfees):
        super().__init__(id1, name1, fees1)
        self.practicalfees = practicalfees

    def calfees(self):
        print(f"Final fees of Medical={self.fees + self.practicalfees}")

    def __str__(self):
        return super().__str__() + f"\tPractical Fees={self.practicalfees}"
    
    def display(self):
        print(f"Practical Fees={self.practicalfees}")
        super().display()
s1 = Student(10, "Amit", 20000)
#e1 = EngineeringStudent(11, "Rahul", 60000, 5000)
m1 = MedicalStudent(12, "Priya", 80000, 10000)

print(s1)
#print(e1)
print(m1)'''


#----------------------------------
'''from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

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

    @abstractmethod
    def calFees(self):
        pass

    def __str__(self):
        return f'Id={self.id}\tName={self.name}\tSal={self.sal}'
    def display(self):
        print(f'Id={self.id}\tName={self.name}\tSal={self.sal}')

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def getcom(self):
        return self.com
    def setcom(self,newcom):
        self.com=newcom

    def calsal(self):
        print(f'Final salary of Hr {self.sal + self.com}')

    def __str__(self):
        return super().__str__() + f'\tcommision={self.com}'

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
        print(f'final salary of Devloper {self.sal + self.Bonus}')

    def __str__(self):
        return super().__str__() + f'\tBonus={self.Bonus}'

    def display(self):
        print(f'Bonus={self.Bonus}')
        return super().display()

#class Devloper ends here.........
e1=Employee(11,'ganesh',70000)
h1=Hr(12,'Vikas',150000,25000)
d1=Devloper(13,'shubham',250000,50000)

#print(e1)
print(h1)
print(d1)
'''
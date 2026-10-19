from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,cNo,Color):
        self.cNo=cNo
        self.Color=Color
    def getCno(self):
        return self.cNo
    def setcNO(self,newcNo):
        self.cNo=newcNo
    
    def getColor(self):
        return self.Color
    def setColor(self,newColor):
        self.Color=newColor
    @abstractmethod
    def brake(self):
        pass
    def __str__(self):
        return f'Che No={self.cNo}Color={self.Color}'
class Car(Vehicle):
    def brake(self):
        print('this is the brake of Car')
c=Car(12,'White')
print(c)
c.brake()
        
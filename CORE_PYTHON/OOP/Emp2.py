class Emp:
    def __init__(self,id,name,sal):
        self.__id= id
        self.__name= name
        self. __sal= sal

    def getId(self):
        return self.__id
    def setId(self, newId):
        self.__id = newId

    def __str__(self):
        return f"Id = {self.__id}\tName = {self.__name}\tSalary = {self.__sal}"

class Hr(Emp):
    def __str__(self):
        print(self.__id)
        return super().__str__()
e1= Emp(12,"Ganesh",5000000000)
print(e1)
    

#proctected

"""class Emp:
    def __init__(self,id,name,sal):
        self._id= id
        self._name= name
        self. _sal= sal

    def getId(self):
        return self._id
    def setId(self, newId):
        self._id = newId

    def __str__(self):
        return f"Id = {self._id}\tName = {self._name}\tSalary = {self._sal}"

class Hr(Emp):
    def __str__(self):
        print(self._id)
        return super().__str__()
e1= Emp(12,"Ganesh",5000000000)
print(e1._name)"""
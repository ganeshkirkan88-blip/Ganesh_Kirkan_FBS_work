# single - level inheritance
#     A ---> B
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")
c = Child()
c.func1()  # Calling parent function        


# multilevel inheritance
#     A ---> B ---> C

'''class GrandParent:
    def func1(self):
        print("This function is in grandparent class.")

class Parent(GrandParent):
    def func2(self):
        print("This function is in parent class.")

class Child(Parent):
    def func3(self):
        print("This function is in child class.")

c = Child()
c.func1()  # Calling grandparent function
c.func2()  # Calling parent function
c.func3()  # Calling child function'''

# Hierarchical inheritance
#     A ---> B
#     A ---> C

'''class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child1 class.")

class Child2(Parent):
    def func3(self):
        print("This function is in child2 class.")

c1 = Child1()
c1.func1()  # Calling parent function
c1.func2()  # Calling child1 function

c2 = Child2()
c2.func1()  # Calling parent function
c2.func3()  # Calling child2 function'''

# Multiple inheritance
#     A  + B---> C

'''class Father:
    def func1(self):
        print("This function is in father class.")
        

class Mother:
    def func2(self):
        print("This function is in mother class.")
        

class Child(Father, Mother):
    def func3(self):
        print("This function is in child class.")

c = Child()
c.func1()  # Calling father function
c.func2()  # Calling mother function
c.func3()  # Calling child function'''
'''def add():
    print('I am in add:')
add(1)'''

#self :- self refers to the current object.

class Employee:
    def __init__(self):
        print('I am in constructor of Employee',id(self))
    def display(self):
        print('I am from display of Employee')
e1=Employee()
e2=Employee()
print(f'id e1={id(e1)}')
print(f'id e2={id(e2)}')
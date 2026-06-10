class Student:
    def __init__(self,rollno,name):
        print("Inside Parameterized Constructor")
        self.rollno = rollno
        self.name = name
    def displayStudent(self):
        print('Roll Number =',self.rollno)
        print('Student Name =',self.name)
r = int(input('Enter roll number'))
n = input('Enter name')
s1 = Student(r,n)
s1.displayStudent()
class Atm:
    #constructor(special function)->superpower->
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""
Hi, how can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Press 5 to exit
""")
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            print("Change pin feature not implemented yet")
        elif user_input == '3':
            print("Check balance feature not implemented yet")
        elif user_input == '4':
            print("Withdraw feature not implemented yet")
        elif user_input == '5':
            exit()
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin
        user_balance = int(input("Enter balance: "))
        self.balance = user_balance
        print("PIN created successfully")
        self.menu()
# Create ATM object
atm = Atm()
def __init__add(self,other):
    new_num    = self.num*other.den + other.num*self.den
    new_den = self.den*other.den
    return '()/{}'.format(new_num,new_den)
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
def greet(p):
    print('Hi my name is', p.name, 'and I am a', p.gender)
    p1 = Person('Rahul', 'Male')
    return p1
p = Person('Prashant Pandey', 'Male')
X = greet(p)
print(X.name)
print(X.gender)
#Is Object Mutable
class Cirle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return Circle.pi*self.radius*self.radius
    def circumference(self):
        return 2*Circle.pi*self.radius
    def display(self):
        print("Area ="round(self)
        circumference = self.circumference
        constant.pi = self.constantpi
        area = self.area

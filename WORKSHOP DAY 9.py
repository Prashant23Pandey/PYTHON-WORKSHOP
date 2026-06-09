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

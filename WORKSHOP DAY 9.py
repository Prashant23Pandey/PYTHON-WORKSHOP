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
        

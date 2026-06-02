#Program that generates an increasing ASCII alphabet left triangle
n = 5
for i in range(1, n + 1):
    value = 65
    for j in range(1, i + 1):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
    print()  
#Program to generates an increasing ASCII alphabet left triangle
for i in range(65,91):
    print()
    for j in range(65,i+1):
        print(chr(j),end="")
#Program to generates an ASCII alphabet left triangle each row different alphabet
for i in range(65, 91):  
    print()
    for j in range(65, i+1):
        ch = chr(i)
        print(ch, end=" ")
#Program to generates an Inverted Alphabet Triangle
for i in range(90, 64, -1): 
    print()
    for j in range(65, i+1):
        ch = chr(j)
        print(ch, end=" ")
#Program to sum two numbers
def sum(a,b):
    c = a + b
    print(c)
    return c
sum(2,3)
#Program to call out name
name = str(input("Enter your name: "))
def greet(name):
    print("Hello," + name +". Good Morning!")
    return()
greet(name)
#double underscore
print(greet.__doc__ )
def greet():
    return "Hello. Prashant Pandey"
print(greet())
num = int(input("Enter the number"))
def sqr(num):
    return num**2
print(sqr(num))
print(sqr.__doc__)
#Program to calculate Simple Interest
def sim_int(p,r,t):
    si = p*r*t/100
    return si
s = sim_int(1000,10,3)
print("Simple Interest is=",s)
print("Simple Interest is=",sim_int(500,12,6))
pi = int(input("Enter the Principal: "))
ri = int(input("Enter the Rate: "))
td = int(input("Enter the Time: "))
sim = sim_int(pi,ri,td)
print("Simple Interest is= ",sim)
#Program to find whether x is divisible/not divisible by y
def div(x,y):
    if x%y==0:
        print(x,"is divisible by",y)
    else:
        print(x,"is divisible by",y)
div(12,4)
div(8,3)
div(9999,3)
#Program to Count the number in a Digit
def count(n):
    if n == 0:
        return 1
    n = abs(n)              #converts a negative number to positive
    count = 0
    while n > 0:
        n = n//10
        count += 1  
    return count
number = 232323
print("Number of digits:", count(number))
#Program to Compute Factorial
def fact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
n = int(input("Enter the value of n in nCr: "))
r = int(input("Enter the value of r in nCr: "))
c = fact(n) // (fact(r) * fact(n - r))
print("value of",n,"C",r,"is",c)
#Program to change list
def change(x):
    x[1]="2323"
    print("Value Inside the Function",x)
    return
y = [2322,2325,2324]
print("Before changing the values are: ",y)
change(y)
print("After changing the values are: ",y)
def keyword(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)
    return
keyword(1,2,3)
keyword(a=10,b=20,c=20)
keyword(a=100,b=200,c=200)
#Demo of keyword arguement
def keyword(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)
    return
keyword(100,b=300,a=400)                  #Type Error
def keyword(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)
    return
keyword(a=100,b=300,400)                  #Type Error
DEFAULT ARGUMENT
Demo of default argument
def project(name,language="python"):
    print("project",name,"is developed using",language)
    return
project("Online exam system","java")
project(name="Reservation System",language="C++")
project("Election Data Analysis")
project(language="java")
#Demo of non keyword variable length argument
def var_len(*var):
    print("All the parameters are parked in tuple: ",var)
    print("Accessing tuple elements one by one: ")
    for v in var:
        print(v)
    return
var_len(10)
var_len(10,20,30,40,50)

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



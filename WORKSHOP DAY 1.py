print('Hello World')
print('Prashant Pandey')
print('Prashant',23,31,12,True,sep='/')
print('Prashant',end='-')
print('Pandey')
#Decimal
print(8.23)
#1*10^308
print(1e309)
#list->-C->Array
print([23,24,25,26,27])
#type
a=[1,2,3]
print(type(a))
id(a)
#Dynamic Binding
a=5
print(a)
a='Maneesh'
print(a)
#Static Binding
a=5
#KEYWORDS
import keyword
print(keyword.kwlist)
#Identifiers
#You can't start with a digit
name='Prashant'
print(name)
#You can use special chars->_
_='Prashant'
print(_)
#Take input from users and store them in a variable
fnum = int(input('Enter First Number'))
snum = int(input('Enter Second Number'))
print(type(fnum),type(snum))
#add the two variables
result= fnum + snum
#print result
print(result)
#Arithmetic Operators
print(17+6)
print(32-9)
print(23*1)
print(46/2)
print(46//2)
print(23%3)
print(23**23)
#Relational Operators
print(23>17)
print(23<17)
print(23<+23)
print(23<=23)
print(23==23)
print(23!=23)
#Bitwisw Operators
bitwise and
print(2&3)
bitwise or
print(2|3)
bitwise xor
print(~23)
print(23^8)
print(23<<8)
print(23>>8)
#Assignment Operators
# =
# a=2
a = int(input('Enter Number 1'))
b = int(input('Enter Nymber 2'))
result = a&b-1
print(result)
#Membership Operators
#in/not in
print('D' in 'Delhi')
print(1 in [23,24,25,26])
k = None
a = 23
b = 17
print('Program exe')
a = int(input('Enter a Number 1'))
b = int(input('Enter a Number 2'))
sum = a+b
print(sum)
#Returns 5.0
a = int(input('Enter a number to find its square root'))
result = a ** 0.5
print(result)
a = int(input('Enter the base of the triangle: '))
b = int(input('Enter the height of the triangle: '))
Area = a*b/2
print(Area)
#Python Program to solve quadratic using exponent operator
a = int(input('Enter the value of a'))
b = int(input('Enter the value of b'))
c = int(input('Enter the value of c'))
d = (b**2-4*a*c)**0.5
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print(f"The roots of Equation are{x1} and {x2}")
#Python Program to swap two variables
a = 23
b = 17
print('Before Swaping')
print(f'a = {a}, b = {b}')
temp = a
a = b
b = temp
print('After Swaping')
print(f'a = {a}, b = {b}')
#Python Program to convert Celsius to Farenheit (F = 9*C/5 +32)
temp_C = int(input('Enter the temperature in Celsius'))
temp_F = (9/5)*temp_C + 32
print(f'Converted temperature in Farenheit {temp_F}')
#Python Program to calculate the hypotenuse of a right angled triangle h = (b*b + p*p)**0.5
#Input the lengths of the base and perpendicular
base = float(input("Enter the base: "))
perpendicular = float(input("Enter the perpendicular: "))
#Calculate the hypotenuse using the formula
hypotenuse = (base**2 + perpendicular**2)**0.5
#Display the result
print(f"The hypotenuse of the triangle is: {hypotenuse}")
#Write a Program to check if a number is even or odd
num = int(input('Enter the number: '))
if(num%2)==0:
    print('Number is even')
else:
    print('Number is odd')
#Write a Program to find greater between two Numbers
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
if(num1>num2):
    print(f'{num1} is greater number')
else:
    print(f'{num2} is greater number')

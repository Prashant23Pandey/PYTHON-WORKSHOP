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


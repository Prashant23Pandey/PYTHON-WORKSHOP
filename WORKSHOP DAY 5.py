#Lambda with default arguments:
sid=lambda p,r,t=5: p*r*t/100
print(sid(1000,5,10))
print(sid(5000,5))
#Lambda Function with user defined Function
def multiplier(n):
    return lambda a:a*n
doubler=multiplier(2)
print(doubler(10))
print(doubler(5))
tripler=multiplier(3)
print(tripler(10))
greater=lambda x,y: x if x>y else y
print("Greater Number is: ",greater(12,8))
print("Greater Number is: ",greater(23,31))
print("Greater Number is: ",greater(12,20))
even_odd=lambda x:print('Even') if x%2==0 else print('Odd')
even_odd(23)
even_odd(32)
even_odd(7)
even_odd(17)
kvar=lambda**k: print(k)
kvar()
kvar(a=1,b=2,c=3,d=4,e=5)
add=lambda x=10:(lambda y:x+y)
a=add()
print(a(20))
#Passing Lambda Function to another user defined Function
def show():
    print(a(8))
show(lambda x:x)
#IIFE(Immediately Involved Function Expression)
(lambda x:print(x+1))(22)
(lambda x,y:print(x+y))(17,6)
def double(x):
    return x*2
li=[10,20,30,40,50]
new_list=map(double,li)
print(list(new_list))
PRASHANT = [23, 24, 25, 26, 27]
do_list = list(map(lambda x: x * 2, PRASHANT))
print(do_list)
pli = [1000, 2000, 3000, 4000, 5000]
rli = [5.5, 55, 7, 1.5, 8, 4]
tli = [2, 3, 4, 4, 6]
si_li = list(map(lambda p, r, t: p * r * t / 100, pli, rli, tli))
print(si_li)
cs=[-22,1,-34,45,67,-98,78,11,-65,65]
cs_obj=list(filter(lambda x:x>0,cs))
print("Positive Numbers are: ",cs_obj)
#Example of Reduced() Function
#Sum of all elements
from functools import reduce
morning=[2,4,5,6,7,8,9,1,10]
cs=reduce(lambda x,y : x + y, morning)
print("Sum of elements in list is: ",cs)

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

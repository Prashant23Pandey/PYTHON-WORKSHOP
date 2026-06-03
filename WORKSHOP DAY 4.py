print("Prashant Pandey")
Local Variable and Global Variable
total = 0
def sum(arg1,arg2):
    total = arg1 = arg2
    print("Inside the Function local total: ",total)
    return total
sum(10,20)
print("Outside the function global  total: ",total)
a=50
def scope():
    global a
    a=20
    print("Value of a inside the function: ",a)
    print(id(a))
    return
scope()
print("Value odf outside the function: ",a)
print(id(a))
def fun():
    p=100
    print("Inside Function x=",p)
    return
fun()
print("Outside the Function x=",p)
def g(y):
    print(x)
    print(x+1)
    print(x)
x=5
g(x)
print(x)
def h(y):
    x+=1
    print(x)
x=5
h(x)
print(x)

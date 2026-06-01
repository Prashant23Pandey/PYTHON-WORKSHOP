print('Prashant Pandey')
#Program to find greatest number amoung a,b and c
a = int(input("Enter a Number1: "))
b = int(input("Enter a Number2: "))
c = int(input("Enter a Number3: "))
if(a>b):
    if(a>c):
        print("a is greater number")
    else:
        print("c is greater number")
else:
    print("b is greater number")
#Program to find smallest number amoung a,b and c
a = int(input("Enter a Number1: "))
b = int(input("Enter a Number2: "))
c = int(input("Enter a Number3: "))
if(a>b):
    if(a<c):
        print("a is smallest number")
    else:
        print("c is smallest number")
else:
    print("b is smallest number")
#Program to Login email through password
email = input("Enter an Email: ")
password = input("Enter a strong Password: ")
if email == "prashant" and password == "PRAS23":
    print("Login Successfully")
elif email == "prashant" and password != "PRAS23":
    print("Incorrect Password!")
    password = input("Please re-enter the correct password: ")
    if password == "PRAS23":
        print("Welcome, finally!")
    else:
        print("Beta tumse na ho paayega")
#Write a Program to enter a character and then determine whether its a vowel or digit
str1 = input("Enter a character: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
if str1 in vowels:
    print("It is a vowel")
elif str1 in digits:
    print("It is a digit")
else:
    print("It is neither a vowel nor a digit")
# Input marks for 5 subjects
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 = int(input("Enter marks for Subject 5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
print("Total Marks =", total)
print("Average Marks =", average)
if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
else:
    print("Grade: F")
#Program to Print natural Numbers
n = int(input("Enter a Number"))
i = 1
while(i <= n):
    print(i)
    i = i+1
#Write a Program to compute the sum of factorial
n = int(input("Enter a number: "))
fact = 1
sum_fact = 0
for i in range(1, n + 1):
    fact = fact * i
    sum_fact = sum_fact + fact
print("Sum of factorials =", sum_fact)
#Write a Program to display the first N natural numbers
n = int(input("Enter the value of 'n': "))
print(f"Natural numbers upto {n}:-")
for i in range(1,n+1):
    print(i)
#Program to calculate sum of inputs by user
n = int(input("How many numbers do you want to enter? "))
total = 0
i = 1
##while i <= n:
    num = int(input("Enter a number: "))
    total = total + num
    i += 1
print("Sum of inputs =", total)
#Program to print a table using for loop
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
# Program to compute factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)
#Program to check weather a number is Palindrome or not
num = int(input("Enter a number"))
N = num
reverse = 0
while(N!=0):
    r = N%10
    reverse = reverse*10+r
    N = N//10
print(f"Reverse of {num}: {reverse}")
if(num == reverse):
    print(f"{num} is a palindrome")
else:343
    print(f"{num} is not a palindrome")
#Program to check weather a number is Armstrong or not
num = int(input("Enter a number: "))
temp = num
power = len(str(num))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10
if total == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
#Program to Find the Sum of Even and Odd Numbers Separately
n = int(input("Enter how many numbers: "))
even_sum = 0
odd_sum = 0
for i in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of Even Numbers =", even_sum)
print("Sum of Odd Numbers =", odd_sum)
#Fibonacci Series Program
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#Program to Find Factors of a Number
num = int(input("Enter a number: "))
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
#Print a n×n Matrix with a symbol
n = int(input("Enter numbers of terms"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
#Print a n×n Matrix with a number
n = int(input("Enter numbers of terms"))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
#Print a n×n Matrix within a Floyd's triangle
n = int(input("Enter numbers of terms"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
rows = int(input("Enter a Number"))
number = 1
print("Floyd's Triangle")
for i in range(1, rows + 1):
    for j in range(1 , i + 1):
        print(number, end = "")
        number = number + 1
    print()

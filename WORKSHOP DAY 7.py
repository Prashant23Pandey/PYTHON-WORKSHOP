#Attempt to typpe cast a value of wrong data type
#Exception
1.try:
    #Try some code(user input)
2.except Exception:
    #Handle an Exception
3.finally:
    #Do some clean up
try:
    number=int(input("Enter a number"))
    print(1/number)
except Exception:
    print("Something went wrong")
try:
    number=int(input("Enter a number"))
    print(1/number)
except ZeroDivisionError:
    print("Number cannot be divided by zero")
except ValueError:
    print("You have to provide correct value")
finally:
    print("Program is over")
try:
    fruits=["apple","mango","oranges"]
    index=int(input("Enter the index"))
    print(fruits[index])
except IndexError:
    print("Index is not correct")
except ValueError:
    print("Provide correct value")
try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print("Result =", num1 + num2)
    elif op == "-":
        print("Result =", num1 - num2)
    elif op == "*":
        print("Result =", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num1 / num2)
    else:
        print("Invalid operator")
except ValueError:
    print("Please enter valid numbers")
except Exception as e:
    print("Error:", e)
#raise exception: The raise statement is used to explicitly trigger exception 
def check_age(age):
    if age<18:
        raise ValueError("Age must be 18")
    print("Age is correct")
try:
    check_age(15)
except ValueError as e:
    print("Error:", e)
try:
    followers = int(input("Enter the number of followers: "))
    posts = int(input("Posts uploaded this month: "))
    reels = int(input("Reels uploaded this month: "))
    if followers < 100:
        raise ValueError("Followers must be at least 100")
    print("Profile data accepted")
except ValueError as e:
    print("Error:", e)
Assertions are used to verify assumptions in the code.
try:
    mark = -5
    assert mark >= 0,"Marks cannot be negative"
except AssertionError as e:
    print("Error: ",e)
try:
    attendance = int(input("Enter attendance percentage: "))
    if attendance < 75:
        raise ValueError("Student is detained due to low attendance.")
    print("Student is eligible to appear for exams.")
except ValueError as e:
    print("Error:", e)
try:
    username = input("Enter a unique usernme: ")
    password = input("Enter a unique password: ")
    assert username == "admin","Invalid Username"
    assert password == "python123","Invalid Password"
    print("Login Successfully")
except AssertionError as e:
    print("error",e)
# Python writing files (.txt, .json, .csv)
text_data = "I like pizza"
file_path = "Output.txt"                                #relative path
with open(file_path, "w") as file:
    file.write(text_data)
    print(f"txt file {file_path} is created")
file_path="/User/prashant/Dekstop/Output.txt"
try:
    with open(file_path,"r") as file:
        content= file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
import csv
file_path="/User/prashant/Dekstop/Output.txt"
try:
    with open(file_path."r") as file:
        content= csv
#Delete all files

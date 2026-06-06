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

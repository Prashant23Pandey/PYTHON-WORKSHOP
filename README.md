# PYTHON-WORKSHOP
# Day 1 Python Workshop Notes
## 1. First Python Program
```python
print("Hello World")
```
### Output
```
Hello World
```
`print()` is used to display output on the screen.
---
# 2. Printing Multiple Values
```python
print("Prashant", 23, 31, 12, True)
```
### Using Separator
```python
print("Prashant", 23, 31, 12, True, sep="/")
```
### Output
```
Prashant/23/31/12/True
```
### Using End
```python
print("Prashant", end="-")
print("Pandey")
```
### Output
```
Prashant-Pandey
```
---
# 3. Comments
Single-line comments:
```python
# This is a comment
```
Used for explanation and documentation.
---
# 4. Data Types
## Integer (int)
```python
a = 23
```
Whole numbers.
---
## Float (float)
```python
a = 8.23
```
Decimal values.
---
## Boolean (bool)
```python
True
False
```
Represents logical values.
---
## List (Array-like)
```python
a = [23,24,25,26,27]
```
Stores multiple values.
---
# 5. Scientific Notation
```python
print(1e309)
```
Output:
```
inf
```
`inf` means Infinity.
---
# 6. Type Checking
```python
a = [1,2,3]
print(type(a))
```
Output:
```python
<class 'list'>
```
Common Types:
```python
type(10)      # int
type(5.2)     # float
type(True)    # bool
type("ABC")   # str
```
---
# 7. Dynamic Typing (Dynamic Binding)
Python allows changing variable type.
```python
a = 5
a = "Maneesh"
```
Same variable can store different data types.
---
# 8. Python Keywords
```python
import keyword

print(keyword.kwlist)
```
Keywords are reserved words.
Examples:
```python
if
else
for
while
return
break
continue
True
False
None
```
Cannot be used as variable names.
---
# 9. Identifiers (Variable Names)
Valid:
```python
name = "Prashant"
_prashant = "ABC"
```
Invalid:
```python
1name = "ABC"
```
### Rules
Can contain letters, digits, underscore

Cannot start with digit

Cannot use keywords

Case-sensitive

---
# 10. Taking User Input
```python
num = input("Enter Number")
```
Input is stored as string by default.
---
# 11. Integer Conversion
```python
num = int(input("Enter Number"))
```
Converts input to integer.
---
# 12. Addition Program
```python
fnum = int(input("Enter First Number"))
snum = int(input("Enter Second Number"))
result = fnum + snum
print(result)
```
### Example
Input:
```
23
31
```
Output:
```
54
```
---
# 13. Arithmetic Operators
| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor Division |
| %        | Modulus        |
| **       | Power          |
Examples:
```python
23 + 17
32 - 9
23 * 23
46 / 2
23 % 3
23 ** 23
```
---
# 14. Relational Operators
Used for comparison.
```python
>
<
>=
<=
==
!=
```
Example:
```python
print(23 > 17)
```
Output:
```
True
```
---
# 15. Bitwise Operators
## AND
```python
2 & 3
```
Output:
```
2
```
---
## OR
```python
2 | 3
```
Output:
```
3
```
---
## XOR
```python
2 ^ 3
```
Output:
```
1
```
---
## NOT

```python
~23
```
Output:
```
-24
```
---
## Left Shift
```python
23 << 3
```
---
## Right Shift
```python
23 >> 3
```
---
# 16. Assignment Operator
```python
=
```
Example:
```python
a = 10
```
---
# 17. Membership Operators
### in
```python
1 in [23,24,25,26]
```
Output:
```
False
```
### not in
```python
1 not in [23,24,25,26]
```
Output:
```
True
```
---
# 18. String Membership
```python
'D' in 'Delhi'
```
Output:
```
True
```
---
# 19. Square Root Program
```python
a = int(input("Enter Number"))
result = a ** 0.5
print(result)
```
---
# 20. Area of Triangle
Formula:
genui{"math_block_widget_always_prefetch_v2":{"content":"A=\frac{1}{2}bh"}}
Program:
```python
a = int(input("Enter base"))
b = int(input("Enter height"))
area = a * b / 2
print(area)
```
---
# 21. Quadratic Equation
Standard Form:
genui{"math_block_widget_always_prefetch_v2":{"content":"ax^2+bx+c=0"}}
Discriminant:
D=b^2-4ac
Roots:
genui{"math_block_widget_always_prefetch_v2":{"content":"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}"}}
Program used:
```python
a = int(input())
b = int(input())
c = int(input())
d = (b**2 - 4*a*c)**0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)
print(x1, x2)
```
---
# 22. Swapping Two Variables
```python
a = 23
b = 17
temp = a
a = b
b = temp
```
Before:
```
a = 23
b = 17
```
After:
```
a = 17
b = 23
```
---
# 23. Celsius to Fahrenheit
Formula:
F=\frac{9}{5}C+32
Program:
```python
temp_C = int(input())
temp_F = (9/5) * temp_C + 32
print(temp_F)
```
Example:
```
23°C = 73.4°F
```
---
# 24. Hypotenuse of Right Triangle
Pythagoras Theorem:
genui{"math_block_widget_always_prefetch_v2":{"content":"a^2+b^2=c^2"}}
Program:
```python
base = float(input("Enter base"))
perpendicular = float(input("Enter perpendicular"))
hypotenuse = (base**2 + perpendicular**2)**0.5
print(hypotenuse)
```
Example:
```
Base = 23
Perpendicular = 17
Hypotenuse = 28.60
```
---

<img width="1919" height="1126" alt="Screenshot 2026-05-30 112559" src="https://github.com/user-attachments/assets/1ae35609-7e33-43dc-8e0e-29c5aeb556b9" />

<img width="1919" height="1126" alt="Screenshot 2026-05-30 122005" src="https://github.com/user-attachments/assets/b2e5e9e6-69e1-4ca9-97de-9f5aef86f11e" />

<img width="1919" height="1126" alt="Screenshot 2026-05-30 143043" src="https://github.com/user-attachments/assets/fc28a1d0-df9a-4a1e-9c61-62841474ee73" />

<img width="1919" height="1128" alt="image" src="https://github.com/user-attachments/assets/cc73f69f-b438-4d15-ac81-5ad9e49667ee" />

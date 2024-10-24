# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).


import math
x1=int(input("Enter the value of x1 "))
x2=int(input("Enter the value of x2 "))
y1=int(input("Enter the value of y1 "))
y2=int(input("Enter the value of y2 "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("The distance between the points is:", distance)

# Question 1(ii)
# Write a Python program to find maximum between three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3= int(input("Enter third number: "))
          
if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

print("The maximum number is:", {maximum})

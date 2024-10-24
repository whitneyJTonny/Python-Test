# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

def calculate_sum():
  
   num1 = int(input("Enter the number "))
   num2 = int(input("Enter the number "))
   sum = (num2 + num1)
   print(sum)
calculate_sum()   



   






# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

number = int(input("Enter number  from 1 to 100 divisible by 2 "))
if number / 2:
   print("Required")
else:
   print("Not Required")
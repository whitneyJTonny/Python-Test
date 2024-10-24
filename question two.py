# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

def mark_scored(mark):
    mark_scored = int(input("Enter the mark scored"))
    if mark <= 90:
       print("Grade A")
    elif mark >= 80:
       print("Grade B")
    elif mark >= 70:
       print("Grade C")
    elif mark >= 60:
       print("Grade D")
    elif mark >= 40:
       print("Grade 40")
    else:
       print("Grade F")
mark_scored()
    
    
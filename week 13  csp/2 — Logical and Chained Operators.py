# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

#score calc (short for calculator)
score = int(input("Enter your score (0-100: "))

if 90 <= score <= 100 : 
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("F FOR FAILURE")

# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
number = int(input("Enter your number: "))
if 50 <= number <= 100:
    print("Number is between 50 and 100.")
else:
    print("Number is not between 50 and 100.")

x = int(input("Enter a number: "))
print(50 <= x <= 100)


# Write an expression that checks if a number is NOT equal to 0 and greater than 10
number1 = int(input("What is your number? :"))
if number1 == 0:
    print("Number is equal to 0")
elif number1 > 10:
    print("Number is greater than 10")
else:
    print("Number is not equal to 0, and is not greater than 10")

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:


# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
if number1 > number2:
    if number1 > number3:
        largest_number = number1
    else:
        largest_number = number3
else:
    if number2 > number3:
        largest_number = number2
    else:
        largest_number = number3
# Print the result
print("The largest number is:", largest_number)
 
# control_structures.py

# Task 2: Python Control Structures Challenge

# Asking for user input and checking if the number is even or odd
user_input = int(input("Enter an integer: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Generating a list of even numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

# Printing numbers from 10 down to 1 in reverse order
num = 10
while num > 0:
    print(num)
    num -= 1

# Bonus: Function to classify numbers as even or odd
def classify_number(number):
    return "even" if number % 2 == 0 else "odd"

# Testing the function
print(f"The number {user_input} is {classify_number(user_input)}.")
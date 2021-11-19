"""
Program 2:
Write a program to create a simple calculator that can
add, subtract, multiply or divide 2 variables at a time.
"""

def checkchoice(choice,a,b): # Create a simple calculator function
    if choice == 1: # Checking for addition
        sum = a + b
        print("Sum =",sum)
    elif choice == 2: # Checking for subtraction
        subtract = a - b
        print("Difference =",subtract)
    elif choice == 3: # Checking for multiplication
        multiply = a * b
        print("Product =",multiply)
    elif choice == 4: # Checking for division
        divide = a / b
        print("Quotient =",divide)
    else: # Displayed in case of wrong output
        print("Invalid Input!")

a = int(input("Enter number 1 : ")) # Accepting number 1
b = int(input("Enter number 2 : ")) # Accepting number 2
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Displaying menu below
print("Menu")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
choice = int(input("Enter your choice : "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
checkchoice(choice,a,b)

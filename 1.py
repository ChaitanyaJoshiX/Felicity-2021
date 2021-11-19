"""
Program 1 :
Write a program to enter any sentence and calculate the following:
 a) Total number of digits present in it.
 b) Total number of small letters and capital letters present in it.
 c) Total number of alphabets used in it.
 d) Total number of special characters used in it.
"""
string = input("Enter : ") # Accepting a string
l = len(string)
dig = 0
lowercase = 0
uppercase = 0
alphabets = 0
special = 0
for i in range(l):
    if string[i].isalpha(): # Check for alphabets
        alphabets += 1
        if string[i].islower(): # Check for lower case alphabets
            lowercase += 1
        elif string[i].isupper():  # Check for upper case alphabets
            uppercase += 1

    elif string[i].isdigit():  # Check for numbers
        dig += 1
    else:
        special += 1 # Default condition left for special characters

# Displaying all the details below.
print("Details:")
print("digits =",dig)
print("uppercase =",uppercase)
print("special =",special)
print("lowercase =",lowercase)
print("alphabets =",alphabets)

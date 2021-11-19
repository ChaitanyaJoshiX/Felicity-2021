"""
Program 3:
Write a program to move every character in the following string forward,
by 25 ASCII Values.
Here is your string: "PU[LYOV\ZLJTY"
After converting the ASCII,
append that to "bit.ly/" to search your video for the final task.
"""
string = "PU[LYOV\ZLJTY" # Initializing the string
newstring = ""
l = len(string)

for i in range(l):
    character = string[i] # Extracting the charcter from index
    asciival = ord(character) # Finding the ascii value of it
    asciival += 25 # Move character ahead by 25
    newstring += (chr(asciival)) # Appending result to string

print(newstring)

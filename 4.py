"""
Program 4 :
Write a program to generate possible combinations of the following text "NtDUx2Z".
Once generated, append it to the link "bit.ly/"
The link will lead you to final instructions.
Hint: The first, second, third and fifth letters of the combination are
'2', 'Z', 'U' and 't' respectively.
"""

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

string = "NtDUx2Z"
n = len(string)
a = list(string)
permute(a, 0, n-1)

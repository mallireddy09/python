
PYTHON PROGRAM TO CHECK IF STRING IS PALINDROME OR NOT.
Method 1

-> 1. Find the reverse of string.
-> 2. Check if reverse and original string are same or not.

v = input("Enter a string:")

rev = v[::-1]

if v == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

-> Enter a string:amma
   Palindrome
-> Enter a string:mava
   Not a palindrome

-----------------------------------------------------------------------------------------------

PYTHON PROGRAM TO CHECK A NUMBER IS PALINDROME OR NOT.
Method 2

v = input("Enter a string:")
m = str(v)
rev = m[::-1]

if m == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

-> Enter a string:996699
   Palindrome
-> Enter a string:6649
   Not a palindrome

-----------------------------------------------------------------------------------------------

PYTHON PROGRAM TO CHECK A NUMBER IS PALINDROME OR NOT.
Method 3

n = int(input("Enter a number:"))
temp = n
sum = 0
while(n > 0):
    r = n % 10
    sum = sum * 10 + r
    n = n//10
if(temp == sum):
    print("Palindrome")
else:
    print("Not a palindrome")

-> Enter a number:669966
   Palindrome
-> Enter a number:181318
   Not a palindrome

   -----------------------------------------------------------------------------------------------
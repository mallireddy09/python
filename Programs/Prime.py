
PYHTON PROGRAM TO CHECK GIVEN NUMBER IS PRIME OR NOT.

n = int(input("Enter a number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not a prime")
        break
else:
    print("Prime")

-> Enter a number: 7
   Prime
-> Enter a number: 9
   Not a prime

----------------------------------------------------------------------------------------------------------

n = int(input("Enter a number: "))
flag = False
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
if flag:
     print("Not a prime")
else:
    print("Prime")

-> Enter a number: 7
   Prime
-> Enter a number: 9
   Not a prime

   ----------------------------------------------------------------------------------------------------------

PRINTING PRIME NUMBERS IN GIVEN INTERVAL

lower = int(input("Enter the lower interval:"))
upper = int(input("Enter the upper interval:"))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

->  Enter the lower interval:5
    Enter the upper interval:15
    5
    7
    11
    13




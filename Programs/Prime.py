
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
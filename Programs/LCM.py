
LCM(Least Common Multiple)


n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

for n in range (1, n1*n2 + 1):
    if n % n1 == 0 and n % n2 == 0:
        print("LCM of", n1, "and", n2, "is", n)
        break

->  Enter 1st number: 9
    Enter 2nd number: 18
    LCM of 9 and 18 is 18
    
-----------------------------------------------------------------------------

def LCM(n1, n2):
    if n1 > n2:
        higher = n1
    else:
        higher = n2
    value = higher
    while True:
        if higher % n1 == 0 and higher % n2 == 0:
            print("LCM of", n1, "and", n2, "is", higher)
            break
        else:
            higher = higher + value
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
LCM(n1, n2)

->  Enter 1st number: 9
    Enter 2nd number: 18
    LCM of 9 and 18 is 18

-----------------------------------------------------------------------------

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

if n1 > n2:
    v = n1
else:
    v = n2
    
    while(1):
        if v % n1 == 0 and v % n2 == 0:
            print("LCM of", n1, "and", n2, "is", v)
            break
        else:
            v = v + 1
->  Enter 1st number: 49
    Enter 2nd number: 66
    LCM of 49 and 66 is 3234
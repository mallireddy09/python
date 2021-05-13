

def GCD(n1, n2):                        # def GCD(diividend, divisor):
    if n1 == 0:                                # rem = dividend % divisor  
        return n2                              # if rem == 0:
    else:                                          # return divisor
        return GCD(n2 % n1, n1)                 # return GCD(divisor, rem)

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
print("GCD of", n1, "and", n2, "is", GCD(n1, n2))

->  Enter 1st number: 12
    Enter 2nd number: 24
    GCD of 12 and 24 is 12

-----------------------------------------------------------------------

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

while n1 % n2 != 0:
    temp = n1 % n2
    n1 =  n2
    n2 = temp

print("GCD of", n1, "and", n2, "is", n2)

->  Enter 1st number: 25
    Enter 2nd number: 15
    GCD of 10 and 5 is 5
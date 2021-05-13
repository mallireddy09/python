
n = int(input("Enter a Binary Number: "))

sum = 0
i = 0
while n != 0:
    rem = n % 10
    sum = sum + rem * pow(2, i)
    n = n//10
    i += 1
print("Decimal Number is: ",sum)

->  Enter a Binary Number: 105
    Decimal Number is:  9


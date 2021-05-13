
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

-------------------------------------------------------------------------------------

def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

dec_val = int(input("Enter a Decimal Number: "))
DecimalToBinary (dec_val)

->  Enter a Decimal Number: 7
    0111

--------------------------------------------------------------------

def binaryToDecimal(binary):
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec* pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

# Calling function
binary = int(input("Enter a Binary Number: "))
binaryToDecimal(binary)

->  Enter a Binary Number: 105
    9
----------------------------------------------------------------

# Simple way to convert / Trick

print(int("01001",2))
-> 9
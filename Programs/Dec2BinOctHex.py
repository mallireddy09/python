"""
decimal = int(input("Enter a Decimal Number: "))
convert = int(input("Convert into: [1] Binary, [2] Octal [3] HexaDecimal: \n"))

if convert == 1:
    print("Converted to Binary: ",bin(decimal))
elif convert == 2:
    print("Converted to Octal: ",oct(decimal))
elif convert == 3:
    print("Converted to HexaDecimal: ",hex(decimal))
else:
    print("finised")

->  Enter a Decimal Number: 3
    Convert into: [1] Binary, [2] Octal [3] HexaDecimal:
    1
    Converted to Binary:  0b11

    Convert into: [1] Binary, [2] Octal [3] HexaDecimal:
    2
    Converted to Octal:  0o3

    Convert into: [1] Binary, [2] Octal [3] HexaDecimal: 
    3
    Converted to HexaDecimal:  0x3

-----------------------------------------------------------------------------------------------------------------

decimal = int(input("Enter a Decimal Number: "))

print(bin(decimal), "in Binary.")
print(oct(decimal), "in Octal.")
print(hex(decimal), "in HexaDecimal.")

->  Enter a Decimal Number: 3
    0b11 in Binary.
    0o3 in Octal.
    0x3 in HexaDecimal.
-----------------------------------------------------------------------------------------------------------------

"""
# Python program to convert decimal to binary, octal and hexadecimal 

  
# Function to convert decimal to binary 

def decimal_to_binary(dec): 

    decimal = int(dec) 
    # Prints equivalent decimal 
    print(decimal, " in Binary : ", bin(decimal)) 

  
# Function to convert decimal to octal 

def decimal_to_octal(dec): 
    decimal = int(dec) 
    # Prints equivalent decimal 
    print(decimal, " in Octal : ", oct(decimal)) 

  
# Function to convert decimal to hexadecimal 

def decimal_to_hexadecimal(dec): 
    decimal = int(dec) 
    # Prints equivalent decimal 
    print(decimal, " in Hexadecimal : ", hex(decimal)) 

dec = int(input("Enter a Decimal Number: "))
decimal_to_binary(dec) 
decimal_to_octal(dec) 
decimal_to_hexadecimal(dec)

->  Enter a Decimal Number: 3
    3  in Binary :  0b11
    3  in Octal :  0o3
    3  in Hexadecimal :  0x3

--------------------------------------------------------------------------------------------------------------------------------------------

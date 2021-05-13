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
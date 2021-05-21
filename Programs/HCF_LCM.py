def find_hcf(x,y):
    while(y):
        x, y = y, x % y
    return x

a, b = list(map(int, input().split()))
hcf = find_hcf(a, b)
lcm = (a * b) // hcf

print(f"The HCF of {a} and {b} is {hcf}")
print(f"The LCM of {a} and {b} is {lcm}")

->  18 9
    The HCF of 18 and 9 is 9
    The LCM of 18 and 9 is 18
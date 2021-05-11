

n = int(input("Enter the number: "))
m = str(n)
rev = m[::-1]
print(rev)

->  Enter the number: 987654321
    123456789

-----------------------------------------------------------------------------------------------------------

print(input("Enter the number: ")[::-1])

->  Enter the number: 12345
    54321

-----------------------------------------------------------------------------------------------------------

num = int(input("Enter the number: "))
remainder = 0
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10
print(reverse)

->  Enter the number: 12345
    54321

-----------------------------------------------------------------------------------------------------------

def reverse(num):
    remainder = 0
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        num = num // 10
    return reverse

num = int(input("Enter the number: "))
print(reverse(num))

->  Enter the number: 1234
    4321

-----------------------------------------------------------------------------------------------------------
numbers = list(map(int, input().split()))

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print("Even Numbers :", even)
print("Odd Numbers :", odd)

============== Output =================

66 49 2 31 36 39 51 61
Even Numbers : [66, 2, 36]
Odd Numbers : [49, 31, 39, 51, 61]
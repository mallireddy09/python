
n = list(map(int, input("Enter Numbers : ").split(", ")))

maxi = max(n)
vs = ''

while maxi != 0:
    for i in n:
        if i < maxi:
            vs += ' '
        else:
            vs += '|'
    vs += '\n'
    maxi -= 1

print(vs)
============ Output ===============

Enter Numbers : 4, 2, 1, 6
   |
   |
|  |
|  |
|| |
||||

-------------------------------------------------------------------------------------------

n = list(map(int, input("Enter Numbers : ").split(", ")))
maxi = max(n)
for i in range(maxi):
    for j in range(len(n)):
        if maxi - n[j]>i:
            print(" ",end = "")
            continue
        else:
            print("|", end = "")
            continue
    print("\n")

============ Output ===============

Enter Numbers : 4, 2, 1, 6
   |
   |
|  |
|  |
|| |
||||

--------------------------------------------------------------------------------------------
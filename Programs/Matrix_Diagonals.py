def diagonal(arr):
    s1, s2 = 0, 0

    for i in range(len(arr)):
        s1 = s1 + arr[i][i]
        s2 = s2 + arr[i][len(arr)-1-i]

    return abs(s1-s2)
    
n = int(input("Enter the size of matrix: "))
a = []
for i in range(n):
    arr = list(map(int, input().split()))
    
    a.append(arr)
print(a)
print(diagonal(a))

=============== Output ==================

Enter the size of matrix: 3
3 2 1
4 5 6
7 8 9
[[3, 2, 1], [4, 5, 6], [7, 8, 9]]
4
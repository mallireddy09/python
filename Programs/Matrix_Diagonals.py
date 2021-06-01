def diagonal(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i][i]
    for j in range(len(arr)):
        sum = sum - arr[j][len(arr)-1-j]
    
    return abs(sum)
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
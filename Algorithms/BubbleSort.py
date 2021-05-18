
v = list(map(int, input().split(" ")))
print("Unsorted list: ",v)

#  for i in range(len(v)-1, 0, -1)
for i in range(len(v)-1):

    #  for j in range(i)
    for j in range(len(v)-1):
        
        if v[j] > v[j+1]:
            # swap
            v[j], v[j+1] = v[j+1], v[j]

print("Sorted list: ",v)
            
->  66 49 2 39 61 31 51 36
    Unsorted list:  [66, 49, 2, 39, 61, 31, 51, 36]
    Sorted list:  [2, 31, 36, 39, 49, 51, 61, 66]

----------------------------------------------------------------------------

def BubbleSort(v):
    for i in range(len(v)-1, 0, -1):
        for j in range(i):
            if v[j] > v[j+1]:
                temp = v[j]
                v[j] = v[j+
                v[j+1] = temp 

v = list(map(int, input().split()))
print("Unsorted list: ",v)
BubbleSort(v)
print("Sorted list: ",v)

->  66 49 2 39 61 31 51 36
    Unsorted list:  [66, 49, 2, 39, 61, 31, 51, 36]
    Sorted list:  [2, 31, 36, 39, 49, 51, 61, 66]



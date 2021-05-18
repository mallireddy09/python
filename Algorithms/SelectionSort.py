
def SelectionSort(v):
    
    for i in range(len(v)-1):
        minpos = i
        for j in range(i, len(v)):
            if v[j] < v[minpos]:
                minpos = j
        
        v[i], v[minpos] = v[minpos], v[i]

v = list(map(int, input().split()))
print("Unsorted list: ",v)
SelectionSort(v)
print("Sorted list: ",v)

->  66 49 2 39 61 31 51 36
    Unsorted list:  [66, 49, 2, 39, 61, 31, 51, 36]
    Sorted list:  [2, 31, 36, 39, 49, 51, 61, 66]

-------------------------------------------------------------------------------------

## Using min() method

v = list(map(int, input().split()))
print("Unsorted list: ",v)

for i in range(len(v)):
    min_value = min(v[i:])
    min_index = v.index(min_value)
    v[i], v[min_index] = v[min_index], v[i]

print("Sorted list: ",v)

->  66 49 2 39 61 31 51 36
    Unsorted list:  [66, 49, 2, 39, 61, 31, 51, 36]
    Sorted list:  [2, 31, 36, 39, 49, 51, 61, 66]

---------------------------------------------------------------------------------------------



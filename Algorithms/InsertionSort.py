def InsertionSort(v):
    for index in range(1, len(v)):
        key = v[index]
        pos = index 
        while key < v[pos-1] and pos > 0:
            v[pos] = v[pos-1]
            pos = pos-1
        v[pos] = key

v = list(map(int, input().split()))
print("Unsorted list :",v)
InsertionSort(v)
print("Sorted list: ",v)

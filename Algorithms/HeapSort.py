def max_heap(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[largest] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr, n, largest)
  
def HeapSort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n//2, -1, -1):
        max_heap(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Max_Heap root element
        max_heap(arr, i, 0)
  
arr = list(map(int, input().split()))
print("Unsorted Array :",arr)
HeapSort(arr)
print("Sorted Arry :",arr)

->  66 49 51 2 61 31 39 36
    Unsorted Array : [66, 49, 51, 2, 61, 31, 39, 36]
    Sorted Arry : [2, 31, 36, 39, 49, 51, 61, 66]
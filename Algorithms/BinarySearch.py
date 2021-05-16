# Itterative Binary Search

def BinarySearch(list, key):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
    
        if key > list[mid]:
            low = mid + 1   # low = low + mid

        elif key < list[mid]:
            high = mid - 1  # high = high - mid

        else:
            print(key, "found at position", mid)
            break
    if low > high:
        print("Element not found")

list = list(map(int, input().split(" ")))
print(list)
list.sort()
print(list)
key = int(input("Enter the key value: "))
BinarySearch(list, key)

->  66 49 61 36 2 51 31 39
    [66, 49, 61, 36, 2, 51, 31, 39]
    [2, 31, 36, 39, 49, 51, 61, 66]
    Enter the key value: 49
    49 found at position 4

->  66 49 36 2 51 31 39
    [66, 49, 36, 2, 51, 31, 39]
    [2, 31, 36, 39, 49, 51, 66]
    Enter the key value: 9
    Element not found
    
----------------------------------------------------------------------------

# Recursive Binary Search

def BinarySearch(list, low, high, key):
    if high >= low:
        mid = (low + high)//2

        if key < list[mid]:
            return BinarySearch(list, low, mid - 1, key)
        elif key > list[mid]:
            return BinarySearch(list, mid + 1, high, key)
        else:
            print(key, "found at position", mid)
            
    if low > high:
        print("Element not found")

list = list(map(int, input().split(" ")))
print(list)
list.sort()
print(list)
key = int(input("Enter the key value: "))
BinarySearch(list, 0, len(list) - 1, key)

->  66 49 36 2 51 31 39
    [66, 49, 36, 2, 51, 31, 39]
    [2, 31, 36, 39, 49, 51, 66]
    Enter the key value: 2
    2 found at position 0
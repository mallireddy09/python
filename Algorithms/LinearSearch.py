
list = [31, 36, 39, 49, 51, 61, 66]
print(list)
key = int(input("Enter the key value: "))

for i in range(len(list)):
    if key == list[i]:
        print(key, "found at position ",i)
        break
else:
        print("key value not found")

->  [31, 36, 39, 49, 51, 61, 66]
    Enter the key value: 49
    49 found at position  3

---------------------------------------------------------------------
# function

def search(list, key):
    i = 0
    for i in range(len(list)):
        if list[i] == key:
            print(key, "found at position ",i)
            break
    else:
        print("key value not found")

list = [31, 36, 39, 49, 51, 61, 66]
print(list)
key = int(input("Enter the key value: "))
search(list, key)
->  [31, 36, 39, 49, 51, 61, 66]
    Enter the key value: 66
    66 found at position  6    

---------------------------------------------------------------------

# duplicate elements in the list

def search(list, key):
    i = 0
    list1 = []
    flag = False

    for i in range(len(list)):
        if list[i] == key:
            flag = True
            list1.append(i)
    
    if flag == True:
        print(key, "found at position: ")
        for i in list1:
            print(i, end=" ")
    else:
        print("key value not found")

list = [31, 36, 39, 66, 49, 51, 61, 66]
print(list)
key = int(input("Enter the key value: "))
search(list, key)

->  [31, 36, 39, 66, 49, 51, 61, 66]
    Enter the key value: 66
    66 found at position: 
    3 7

---------------------------------------------------------------------

# While

def search(list, key):
    i = 0
    while i < len(list):
        if list[i] == key:
            print(key, "found at position ", i)
        i = i + 1

search([31, 36, 39, 49, 51, 61, 66], 49)

-> 49 found at position  3

---------------------------------------------------------------------
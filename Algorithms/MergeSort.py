def MergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]
        MergeSort(left_list)
        MergeSort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):

            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list[k] = right_list[j]
                j = j+1
                k = k+1

        while i < len(left_list):
            list[k] = left_list[i]
            i = i+1
            k = k+1

        while j < len(right_list):
            list[k] = right_list[j]
            j = j+1
            k = k+1

v = int(input("Elements in list :"))
list = [int(input()) for x in range(v)]
print("Unsorted List :",list)
MergeSort(list)
print("Sorted List :",list)

->  Elements in list :8
    66
    49
    31
    2
    36
    39
    61
    51
    Unsorted List : [66, 49, 31, 2, 36, 39, 61, 51]
    Sorted List : [2, 31, 36, 39, 49, 51, 61, 66]
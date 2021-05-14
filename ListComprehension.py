
# List Comprehension

List comprehensions provide a concise way to create lists. 
It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The expressions can be anything, meaning you can put in all kinds of objects in lists.


# [1, 4, 9, 16, 25, 36]

# Example without List Comprehension:
v = []
for x in range(1,7):
    v.append(x ** 2)
print(v)
-> [1, 4, 9, 16, 25, 36]

# Example with List Comprehension:
v = [x ** 2 for x in range(1,7)]
print(v)
-> [1, 4, 9, 16, 25, 36]

-----------------------------------------------------------

# [36, 25, 16, 9, 4, 1]

# Example without List Comprehension:
v = []
for x in range(6, 0, -1):
    v.append(x ** 2)
print(v)
-> [36, 25, 16, 9, 4, 1]

# Example with List Comprehension:
v = [x ** 2 for x in range(6, 0, -1)]
print(v)
-> [36, 25, 16, 9, 4, 1]

--------------------------------------------------------------

# Example without List Comprehension:
lst1 = []
def lst_square(lst):
    for x in lst:
        lst1.append(x * x)
    return lst1
lst_square([1, 2, 3, 4, 5, 6, 7])
-> [1, 4, 9, 16, 25, 36, 49]

# Example with List Comprehension:
lst = [1, 2, 3, 4, 5, 6, 7]
lst1 = [x * x for x in lst]
print(lst1)
-> [1, 4, 9, 16, 25, 36, 49]

# Example with List Comprehension:
# To get odd numbers:

lst = [1, 2, 3, 4, 5, 6, 7]
lst1 = [x * x for x in lst if x%2 != 0]
print(lst1)
-> [1, 9, 25, 49]
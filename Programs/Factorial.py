PRINTING FACTORIAL NUMBER USING FUNCTIONS.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

n = int(input("Enter the number: "))
result = factorial(n)
print(result)

->  Enter the number: 5
    120

--------------------------------------------------------------------------------------------------

PRINTING FACTORIAL NUMBER. 

n = int(input("Enter the number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)

->  Enter the number: 5
    120

--------------------------------------------------------------------------------------------------

PRINTING FACTORIAL NUMBER USING RECURSION.

def rec_fact(n):
    if n == 0:
        return 1
    else:
        return n * rec_fact(n-1)

n = int(input("Enter the number: "))
result = rec_fact(n)
print(result)

->  Enter the number: 5
    120

--------------------------------------------------------------------------------------------------

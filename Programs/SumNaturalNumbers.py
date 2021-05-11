# print N natural numbers

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end = " ")

->  Enter a number: 10
    1 2 3 4 5 6 7 8 9 10 

---------------------------------------------------------------------------------------------------------------------------------

# Using for loop

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("sum of numbers upto ", n,"are ", sum)

->  Enter a number: 6
    sum of numbers upto 6 are 21

---------------------------------------------------------------------------------------------------------------------------------

# using while loop
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i = i + 1
print("sum of numbers upto ",n,"are ",sum)

->  Enter a number: 3
    sum of numbers upto 3 are 6

---------------------------------------------------------------------------------------------------------------------------------

# using functions

def sum(n):
    return n*(n+1)//2
    
n = int(input("Enter a number: "))
if n > 0:
    print("sum of numbers upto ",n,"are ",sum(n))

->  Enter a number: 9
    sum of numbers upto 9 are 45

 ---------------------------------------------------------------------------------------------------------------------------------

 # sum of 1st 10 natural numbers.
print(sum([*range(11)]))
->  55

---------------------------------------------------------------------------------------------------------------------------------


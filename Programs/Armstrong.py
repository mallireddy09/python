Armstrong Number :
-> Number of n digits which are equal to 
   sum of n th power of its digits.

abcd... = a^n + b^n + c^n + d^n +.....

Example:
     153 = 1^3 + 5^3 + 3^3
         = 153

------------------------------------------------------------------------------------------

Program to check Armstrong number or not

num = int(input("Enter a number: "))
n = len(str(num))
i = num
sum = 0
   
while(i!= 0): 
    digit = i % 10
    sum = sum + digit ** n
    i = i // 10

if sum == num:
    print(num, 'is an Armstrong number')
else:
    print(num, 'is not an Armstrong number')

->  Enter a number: 153
    153 is an Armstrong number
->  Enter a number: 66
    66 is not an Armstrong number

------------------------------------------------------------------------------------------

Program to find Armstrong number in an interval

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

for num in range(lower, upper + 1):
    n = len(str(num))
    i = num
    sum = 0
    
    while(i!= 0): 
        digit = i % 10
        sum = sum + digit ** n
        i = i // 10

    if sum == num:
        print(num)
    
->  Enter lower bound: 100
    Enter upper bound: 1000
    153
    370
    371
    407

------------------------------------------------------------------------------------------
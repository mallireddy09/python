
PRINT FIBONACCI SERIES.

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
fib(5)

->  0
    1
    1
    2
    3

---------------------------------------------------------------------------------------------------------------
PRINT FIBONACII SERIES FOR INPUT 1 AND SO ON.

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(1)

->  0

---------------------------------------------------------------------------------------------------------------------------------
PRINT FIBONACII SERIES FOR -VE VALUES.
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 1:
        print('invalid input')
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
fib(-4)

-> invalid input

---------------------------------------------------------------------------------------------------------------------------------------
PRINT FIBONACCI SERIES.

n = int(input("Enter a number: "))
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first
    first = second
    second = temp + second
-> Enter a number: 5
    0
    1
    1
    2
    3  
    

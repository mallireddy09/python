

Prime Factorization: A method through which a number can be expressed 
as a product of prime numers.

START

1. CHECK IF THE NUMBER IS DIVISIBLE BY 2

2. IF IT IS DIVISIBLE, DIVIDE, ELSE TRY WITH

NEXT PRIME NUMBER

3. REPEAT STEPS STEPS 1-2 UNTIL THE RESULT OF OF DIVISION IS = 1.

END

------------------------------------------------------------------------------

def prime_fact(n):
    prime_factors = []
    divisor = 2
    while divisor <= n:
        if n%divisor == 0:
            prime_factors.append(divisor)
            n = n/divisor
        else:
            divisor += 1
    return prime_factors

n = int(input("Enter a number: "))
print(prime_fact(n))

->  Enter a number: 630
    [2, 3, 3, 5, 7]

--------------------------------------------------------------------------------

n = int(input("Enter a numer: "))
i = 2
while n != 1:
    rem = n % i
    if rem == 0:
        n = n/i
        print(i, end = " ")
    else:
        i = i + 1
    
->  Enter a numer: 630
    2 3 3 5 7 

## Conditions 
-> Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

-> These conditions can be used in several ways,
   most commonly in "if statements" and loops.
-> An "if statement" is written by using the if keyword.

---------------------------------------------------------------------------------------------------------------------------------------

# If statement:

a = 46
b = 96
if b > a:
    print("b is greater than a")
-> b is greater than a

# elif statement:
# "if the previous conditions were not true, then try this condition".

a = 6649
b = 6649
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
-> a and b are equal

---------------------------------------------------------------------------------------------------------------------------------------

# Else

a = 66
b = 49
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
-> a is greater than b

#  Nested If
-> if statements inside if statements.

x = 66
if x > 49:
  print("Above 18,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

-> Above 18,
   and also above 20!

---------------------------------------------------------------------------------------------------------------------------------------

# One line if statement:
a = 66
b = 49
if a > b: print("a is greater than b")
-> a is greater than b

# One line if else statement:
a = 49
b = 66
print("A") if a > b else print("B")
-> B

# One line if else statement, with 3 conditions:
a = 4966
b = 4966
print("A") if a > b else print("Good") if a == b else print("B")
-> Good

-------------------------------------------------------------------------------------------------------------------------------------------

## logical operator

# And
a = 409
b = 66
c = 606
if a > b and c > a:
    print("Both conditions are True")
-> Both conditions are True

# Or
a = 409
b = 66
c = 606
if a > b or a > c:
    print("At least one of the conditions is True")
-> At least one of the conditions is True

------------------------------------------------------------------------------------------------------------------------------------------

# pass Statement
a = 46
b = 96
if b > a:
    pass

------------------------------------------------------------------------------------------------------------------------------------------
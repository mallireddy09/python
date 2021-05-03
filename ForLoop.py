
# For Loops
-> A for loop is used for iterating over a sequence
-> It execute a set of statements, once for each item 
   in a list, tuple, set etc.

bikes = ["Triumph", "Ducati", "Harley Davidson"]
for x in bikes:
    print(x)

->  Triumph
    Ducati
    Harley Davidson

--------------------------------------------------------------------------------------------------------------------------------

# Looping Through a String

for x in "bike":
    print(x)

->  b
    i
    k
    e

--------------------------------------------------------------------------------------------------------------------------------

# break Statement
bikes = ["Triumph", "Ducati", "Harley Davidson"]
for x in bikes:
    print(x)
    if x == "Ducati":
        break

->  Triumph
    Ducati

bikes = ["Triumph", "Ducati", "Harley Davidson"]
for x in bikes:
    if x == "Ducati":
        break  # but this time the break comes before the print.
    print(x) 

-> Triumph
--------------------------------------------------------------------------------------------------------------------------------

# continue Statement

bikes = ["Triumph", "Ducati", "Harley Davidson"]
for x in bikes:
    if x == "Ducati":
        continue
    print(x)

->  Triumph
    Harley Davidson
--------------------------------------------------------------------------------------------------------------------------------

# range() Function

-> loop through a set of code a specified number of times,
  we can use the range() function,
-> range() function returns a sequence of numbers,
   starting from 0 by default, and increments by 1 (by default), 
   and ends at a specified number.

# 1. Using the range() function:

for x in range(6):
    print(x, end=" ")
-> 0 1 2 3 4 5

# 2. Using the start parameter:

for x in range(2, 6):
    print(x, end=" ")
-> 2 3 4 5 

# 3. Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
    print(x, end=" ")
-> 2 5 8 11 14 17 20 23 26 29 

--------------------------------------------------------------------------------------------------------------------------------

# Else in For Loop

-> else keyword in a for loop specifies a block of code
   to be executed when the loop is finished.

for x in range(6):
  print(x, end = " ")
else:
  print("Finished!")

-> 0 1 2 3 4 5 Finished!

-> else block will NOT be executed,
   if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finished!")

->  0
    1
    2
--------------------------------------------------------------------------------------------------------------------------------

# Nested Loops

-> It is a loop inside a loop.
-> The "inner loop" will be executed one time 
   for each iteration of the "outer loop".

hero = ["PSPK", "SSMB"]
movie = ["Thammudu", "Pokiri"]
for x in hero:
    for y in movie:
        print(x, y)

->  PSPK Thammudu
    PSPK Pokiri
    SSMB Thammudu
    SSMB Pokiri
--------------------------------------------------------------------------------------------------------------------------------

# pass Statement
for x in [0, 1, 2]:
    pass

--------------------------------------------------------------------------------------------------------------------------------

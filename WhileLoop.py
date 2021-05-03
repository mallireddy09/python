
# Python Loops
-> Python has two primitive loop commands:
   1. while loops
   2. for loops

# while Loop
-> It execute a set of statements as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1

->  1
    2
    3
    4
    5

------------------------------------------------------------------------------------------------------------------------------------------

# break Statement
-> break statement it can stop the loop even if the 
   while condition is true.

i = 1
while i < 6:
  print(i)
  if i == 3:  # Exit the loop when i is 3
    break
  i += 1

  -> 1
     2
     3

---------------------------------------------------------------------------------------------------------------------------------------------

# continue Statement
-> continue statement we can stop the current iteration, 
   and continue with the next.

i = 0
while i < 6:
  i += 1
  if i == 3: # Continue to the next iteration if i is 3
    continue
  print(i)

->  1
    2
    4
    5
    6

---------------------------------------------------------------------------------------------------------------------------------------------

# else Statement
-> else statement we can run a block of code 
   once when the condition no longer is true.

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") 

->  1
    2
    3
    4
    5
    i is no longer less than 6

---------------------------------------------------------------------------------------------------------------------------------------------
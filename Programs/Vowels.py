

sentence = input("Enter the sentence: ")
string = sentence.lower()
print(string)
count = 0
list1 = ["a", "e", "i", "o", "u"]
for char in string:
    if char in list1:
        count = count + 1

print("No.of vowels in given sentence is: ",count)

->  Enter the sentence: Hello Welcome to InsanePython
    hello welcome to insanepython
    No.of vowels in given sentence is:  10

    ----------------------------------------------------------------------------------------------
    

PROGRAM TO COUNT LETTERS AND DIGITS IN A STRING:

def letters_digits(string):
    letter = digit = 0

    for i in string:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            letter += 1
    return letter, digit

string = input("Enter a string: ")
letters, digits = letters_digits(string)

print("No.of letters/alphabets: ",letters)
print("No.of digits: ",digits)

->  Enter a string: insanepython09
    No.of letters/alphabets:  12
    No.of digits:  2
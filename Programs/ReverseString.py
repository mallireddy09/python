

print(input("Enter a string: ")[::-1])

->  Enter a string: love
    evol

--------------------------------------------------------------------------

def rev(string):
    reverse = " "
    for i in string:
        reverse = i + reverse
    print(reverse)

string = input("Enter a string: ")
rev(string)

->  Enter a string: love
    evol

--------------------------------------------------------------------------

string = input("Enter a string: ")
rev = " "
for i in string:
    rev = i + rev
print(rev)

->  Enter a string: love
    evol

--------------------------------------------------------------------------
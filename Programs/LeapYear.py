PROGRAM TO CHECK GIVEN YEAR IS LEAP YEAR OR NOT
# METHOD 1

year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

->  Enter the year: 2020
    2020 is a leap year
->  Enter the year: 2021
    2021 is not a leap year

-------------------------------------------------------------------
PROGRAM TO CHECK GIVEN YEAR IS LEAP YEAR OR NOT
# METHOD 2

year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,"is a leap year")
else:
    print(year, "is not a leap year")

->  Enter the year: 1999
    1999 is not a leap year
->  Enter the year: 2000
    2000 is a leap year

-----------------------------------------------------------------------------
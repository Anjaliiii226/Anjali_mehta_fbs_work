def leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if leap(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")
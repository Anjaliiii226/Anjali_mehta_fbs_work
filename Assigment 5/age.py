gender= input("Enter the gender:")
age = int(input("Enter the age:"))

if((gender == 'M' and age >=21) or (gender == 'F' and age >=18)):
    print("Eligible for marriage:")
else:
    print("Not eligible for marriage:")

 
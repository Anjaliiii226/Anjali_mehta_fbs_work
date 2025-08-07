basic_salary = int(input("Enter basic salary:"))

if(basic_salary<=5000):

 da = basic_salary * 0.10
 ta = basic_salary * 0.20
 hra = basic_salary * 0.35
else:
    da = basic_salary * 0.10
    ta = basic_salary * 0.20
    hra = basic_salary * 0.25

total_salary = basic_salary + da+ta+hra
print(total_salary )


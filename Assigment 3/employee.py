basic = int(input("Enter basic salary: "))

da = 0.10 * basic   
ta = 0.12 * basic   
hra = 0.15 * basic  


total_salary = basic + da + ta + hra


print(f"Basic Salary    : {basic:}")
print(f"DA (10%)        : {da:}")
print(f"TA (12%)        : {ta:}")
print(f"HRA (15%)       : {hra:}")
print(f"Total Salary    : {total_salary:}")
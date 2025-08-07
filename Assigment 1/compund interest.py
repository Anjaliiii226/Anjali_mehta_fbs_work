P = int(input("Enter Principal amount (P): "))
T = int(input("Enter Time in years (T): "))
R = int(input("Enter Rate of Interest per annum (R): "))

# Calculate compound amount
A = P * (1 + R / 100) ** T

# Calculate compound interest
CI = A - P

# Output the result
print(f" Compound Interest is {P}:")
print(f"Total Amount is {A}:")
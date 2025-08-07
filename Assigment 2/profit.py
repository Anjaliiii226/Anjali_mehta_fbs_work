cp = int(input("Enter the Cost Price (CP): "))
sp = int(input("Enter the Selling Price (SP): "))

if sp > cp:
    profit = sp - cp
    print(f"Profit = {profit}")
elif cp> sp:
    loss = cp - sp
    print(f"Loss = {loss}")
else:
    print("No Profit, No Loss.")
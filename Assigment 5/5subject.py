passengers = int(input("Enter number of passengers: "))
ticket = float(input("Enter per ticket cost: "))

total_amount = 0


for i in range(passengers):
    age = int(input(f"Enter age of passenger : "))
    
    if age < 12:
        fare  = ticket * 0.70  
    elif age > 60:
        fare = ticket * 0.50  
    else:
        fare = ticket  
    
    total_amount += fare


print(f"Total ticket cost for all passengers: Rs. {total_amount:}")
# Predefined exchange rates (base = 1 USD)
exchange_rates = {
    "USD": 1,
    "INR": 83.0,     
    "EUR": 0.92,     
    "GBP": 0.79,     
    "JPY": 150.0     
}

def convert_currency(amount, from_curr, to_curr):
    amount_in_usd = amount / exchange_rates[from_curr]
    
    converted_amount = amount_in_usd * exchange_rates[to_curr]
    
    return converted_amount


def currency_converter():
    print("----- Currency Converter -----")
    print("Available Currencies: USD, INR, EUR, GBP, JPY")

    try:
        amount = float(input("Enter amount: "))
        from_curr = input("Enter FROM currency: ").upper()
        to_curr = input("Enter TO currency: ").upper()

        if from_curr not in exchange_rates or to_curr not in exchange_rates:
            print("\n❌ Invalid currency! Please select from the list: USD, INR, EUR, GBP, JPY")
            return

        result = convert_currency(amount, from_curr, to_curr)
        print(f"\n✔ {amount} {from_curr} = {round(result, 2)} {to_curr}")

    except ValueError:
        print("\n❌ Invalid amount! Please enter a number.")

currency_converter()

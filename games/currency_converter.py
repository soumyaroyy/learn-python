# Convert Currency

exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 75.0},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 88.5},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 100.0},
    'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.01}
}
history = []


def convert(from_currency,to_currency, amount):
    if from_currency == to_currency:
        return amount
    elif from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return amount * exchange_rates[from_currency][to_currency]
    else:
        return  None
    
def add_to_history(amount, from_currency, converted_amount, to_currency):
    result = f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
    print(result)
    history.append(result)

def display_history():
    print("\nConversion History:")
    for record in history:
        print(record)

while True:
    amount = int(input('Enter the amount: '))
    from_currency = input('Source Currency (USD/EUR/GBP/INR): ').upper()
    to_currency = input('Target Currency (USD/EUR/GBP/INR): ').upper()


    converted_amount = convert(from_currency,to_currency, amount)

    if converted_amount is not None:
        add_to_history(amount, from_currency, converted_amount, to_currency)
    else:
        print("Invalid currency selection or conversion rate not available.")

    more = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if more != 'yes':
        break

display_history()

    
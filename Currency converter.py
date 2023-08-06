def main():
    print("Currency Converter")
    print("Available currencies: EUR, GBP, JPY, INR")

    usd_amount = float(input("Enter amount in USD: "))
    target_currency = input("Enter target currency (EUR/GBP/JPY/INR): ").upper()

    exchange_rates = {
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 109.69,
        "INR": 73.51  # Example exchange rate (as of the time of writing)
    }

    if target_currency in exchange_rates:
        converted_amount = usd_amount * exchange_rates[target_currency]
        print(f"Converted amount: {converted_amount:.2f} {target_currency}")
    else:
        print("Invalid target currency.")

if __name__ == "__main__":
    main()

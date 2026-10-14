stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        print("Stock:", stock)
        print("Price: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)

        total_investment = total_investment + investment

    else:
        print("Stock not available.")

print("----------------------------")
print("Total Investment: $", total_investment)
print("Thank you for using Stock Portfolio Tracker!")
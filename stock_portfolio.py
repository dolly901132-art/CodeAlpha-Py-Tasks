
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "=", price)

print("\nEnter your stock details.")

number_of_stocks = int(input("How many different stocks do you have? "))

portfolio = {}

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available in our list.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity

    portfolio[stock_name] = {
        "quantity": quantity,
        "price": stock_prices[stock_name],
        "investment": investment
    }

    total_investment += investment

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")

for stock, details in portfolio.items():
    print(
        stock,
        "- Quantity:", details["quantity"],
        "| Price:", details["price"],
        "| Investment:", details["investment"]
    )

print("\nTotal Investment =", total_investment)
print("================================")
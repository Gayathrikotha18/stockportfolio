# Task 2: Stock Portfolio Tracker

# Stock price database
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320
}

print("📊 Stock Portfolio Tracker")

# User input
stock_name = input("Enter stock name (AAPL/TSLA/GOOG/MSFT): ").upper()
quantity = int(input("Enter quantity: "))

# Check and calculate
if stock_name in stocks:
    price = stocks[stock_name]
    total = price * quantity

    print("\n💰 Stock Details")
    print("----------------")
    print("Stock Name:", stock_name)
    print("Price per Share:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total)

else:
    print("❌ Invalid stock name! Please try again.")
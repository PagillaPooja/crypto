import requests

# Function to get live price from CoinGecko API
def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"
    response = requests.get(url)
    data = response.json()
    return data[coin]["inr"]

# Portfolio dictionary
portfolio = {}

# Taking user input
n = int(input("Enter number of cryptocurrencies: "))

for i in range(n):
    coin = input("Enter coin name (bitcoin, ethereum, etc): ").lower()
    quantity = float(input("Enter quantity: "))
    buy_price = float(input("Enter buying price (INR): "))
    
    portfolio[coin] = {
        "quantity": quantity,
        "buy_price": buy_price
    }

# Calculate portfolio value
total_value = 0
total_investment = 0

print("\n----- Portfolio Summary -----")

for coin, details in portfolio.items():
    current_price = get_price(coin)
    quantity = details["quantity"]
    buy_price = details["buy_price"]
    
    current_value = current_price * quantity
    investment = buy_price * quantity
    profit_loss = current_value - investment

    total_value += current_value
    total_investment += investment

    print(f"\nCoin: {coin.capitalize()}")
    print(f"Current Price: ₹{current_price}")
    print(f"Value: ₹{current_value}")
    print(f"Profit/Loss: ₹{profit_loss}")

# Final summary
print("\n===== Total Portfolio =====")
print(f"Total Investment: ₹{total_investment}")
print(f"Current Value: ₹{total_value}")
print(f"Overall Profit/Loss: ₹{total_value - total_investment}")
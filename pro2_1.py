import time

def print_details(trader_balance,market_balance,broker_balance,market_bitcoin_holdings,market_temp_holdings):
    print("Trader's virtual bank account balance: ", trader_balance, "USDC")
    print("Market's virtual bank account balance: ", market_balance, "USDC")
    print("Broker's virtual bank account balance: ", broker_balance, "USDC")
    print("Market's bitcoin holdings: ", market_bitcoin_holdings, "BTC")
    print("Market's temporary holdings: ", market_temp_holdings, "BTC")


# Define the initial balance of each party
trader_balance = 100000
market_balance = 100000
broker_balance = 100000

# Define the market's holdings of bitcoin
market_bitcoin_holdings = 100000
market_temp_holdings = 0

# Define the price of 1 bitcoin in USDC
bitcoin_price = 1

brokerage_fees=200

# Keep track of the number of trades
count_buy = 0
count_sell=0

# Maximum number of trades to be executed
max_buy = 5
print_details(trader_balance, market_balance, broker_balance, market_bitcoin_holdings, market_temp_holdings)
print("\n")
print("Trading will start in 10 sec.....")

time.sleep(10)

while count_buy < max_buy:
    # Display the virtual bank account balance for each party
    

    # Display the price of 1 bitcoin in USDC
    

    # Buy 5,000 shares
    count_buy+=1
    shares = 5000
    cost = shares * bitcoin_price
    if trader_balance >= cost:
        # Deduct the cost from the trader's balance
        trader_balance -= cost

        if(count_buy==1):
         trader_balance -=brokerage_fees   
         broker_balance = broker_balance + brokerage_fees
         market_balance +=cost
        else:
            market_balance+=cost

        # Add the shares to the trader's holdings
        market_bitcoin_holdings-=shares
        market_temp_holdings += shares

        

        print("\nYou have successfully bought", shares, "shares for", cost, "USDC.")
        print_details(trader_balance, market_balance, broker_balance, market_bitcoin_holdings, market_temp_holdings)
        
        
        
        # Increase the trade count
        

    # Wait for 1 minute before the next trade
    time.sleep(30)

# Wait for 5 minutes before selling the shares

# Sell 15,000 shares
count_sell+=1
shares = 15000
if shares <= market_temp_holdings:
    
    # Deduct the shares from the trader's holdings
    market_temp_holdings -= shares
    market_bitcoin_holdings+=shares

    # Calculate the revenue from selling the shares
    revenue = shares * bitcoin_price

    # Add the revenue to the trader's balance
    trader_balance += revenue

    if(count_sell==1):
         trader_balance -= brokerage_fees
         broker_balance  +=brokerage_fees
         market_balance = market_balance-revenue
    else:
            market_balance-=revenue

    print("\nYou have successfully sold", shares, "shares for", revenue, "USDC.")
    print_details(trader_balance, market_balance, broker_balance, market_bitcoin_holdings, market_temp_holdings)

    # Update the price of 1 bitcoin in USDC based on the latest trade
    
else:
    print("\nYou do not have enough shares to sell.")

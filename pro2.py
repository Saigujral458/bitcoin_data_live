
trader_balance = 100000
market_balance = 100000
broker_balance = 100000


market_bitcoin_holdings = 100000
market_temp_holdings = 0


bitcoin_price = 1

count_buy=0
count_sell=0
brokerage_fees=200


print("Trader's virtual bank account balance: ", trader_balance, "USDC")
print("Market's virtual bank account balance: ", market_balance, "USDC")
print("Broker's virtual bank account balance: ", broker_balance, "USDC")

# Display the market's holdings account
print("Market's bitcoin holdings: ", market_bitcoin_holdings, "BTC")
print("Market's temporary holdings: ", market_temp_holdings, "BTC")

# Display the price of 1 bitcoin in USDC
print("Price of 1 bitcoin: ", bitcoin_price, "USDC")

while True:

# Ask the user if they want to buy or sell stocks
 action = input("Do you want to buy or sell stocks? (Enter 'buy' or 'sell'or'exit'): ")

# If the user wants to buy stocks
 if action.lower() == "buy":
    count_buy +=1
    # Ask the user how many shares they want to buy
    shares = int(input("How many shares do you want to buy? "))

    # Calculate the cost of the shares
    cost = shares * bitcoin_price

    # Check if the trader has enough funds to buy the shares
    if trader_balance < cost:
        print("You do not have enough funds to buy these shares.")
    else:
        # Deduct the cost from the trader's balance
        trader_balance -= cost
        market_bitcoin_holdings -= shares
        # Add the shares to the trader's holdings
        market_temp_holdings += shares
        
        # Add the funds to the broker's balance
        if(count_buy==1):
         trader_balance -=brokerage_fees   
         broker_balance = broker_balance + brokerage_fees
         market_balance +=cost
        else:
            market_balance+=cost

        print("You have successfully bought", shares, "shares for", cost, "USDC.")
        print("Trader's virtual bank account balance: ", trader_balance, "USDC")
        print("Broker's virtual bank account balance: ", broker_balance, "USDC")
        print("Market's virtual bank account balance: ", market_balance, "USDC")
        print("Market's bitcoin holdings: ", market_bitcoin_holdings, "BTC")
        print("Market's temporary holdings: ", market_temp_holdings, "BTC")

# If the user wants to sell stocks
 elif action.lower() == "sell":
    count_sell +=1
    # Ask the user how many shares they want to sell
    shares = int(input("How many shares do you want to sell? "))

    # Check if the trader has enough shares to sell
    if market_temp_holdings < shares:
        print("You do not have enough shares to sell.")
    else:
        # Deduct the shares from the trader's holdings
        market_temp_holdings -= shares
        market_bitcoin_holdings +=shares

        # Calculate the earnings from the sale
        earnings = shares * bitcoin_price

        # Add the earnings to the trader's balance
        trader_balance += earnings

        # Deduct the earnings from the brokers's balance
        if(count_sell==1):
         trader_balance -= brokerage_fees
         broker_balance  +=brokerage_fees
         market_balance = market_balance-earnings
        else:
            market_balance-=earnings 

        print("You have successfully sold", shares, "shares for", earnings, "USDC.")
        print("Trader's virtual bank account balance: ", trader_balance, "USDC.")
        print("Broker's virtual bank account balance: ", broker_balance, "USDC")
        print("Market's virtual bank account balance: ", market_balance, "USDC")
        print("Market's bitcoin holdings: ", market_bitcoin_holdings, "BTC")
        print("Market's temporary holdings: ", market_temp_holdings, "BTC")
 elif action.lower() == "quit":
    print("\nExiting program. Have a great day!")
    break        
 
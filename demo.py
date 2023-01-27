import ccxt 
import time
import sqlite3
from datetime import datetime

# Connect to or create a database named 'crypto.db'
conn = sqlite3.connect('crypto.db')
c = conn.cursor()

# Create a table named 'crypto_data' with the following columns:
c.execute('''CREATE TABLE IF NOT EXISTS crypto_data
             (Time text, open_price real, current_price real, percent_change_last real, percent_change_open real)''')

binance = ccxt.binance()

ticker = binance.fetch_ticker('BTC/USDT')

last_price = 0
open_price = ticker['open']

try:
    while True:
        ticker = binance.fetch_ticker('BTC/USDT')

        timestamp = ticker['timestamp']
        dt_object = datetime.fromtimestamp(timestamp / 1000)
        Time = f"{dt_object.hour}:{dt_object.minute}:{dt_object.second}"
        print("Time:", dt_object.hour, ":", dt_object.minute, ":", dt_object.second,end='|')
        print("Open Price: ", open_price, end=' | ')
        
        current_price = ticker['last']
        print("Current Price: ", current_price, end=' | ')
        if last_price != 0:
            percent_change_last = round(((current_price - last_price) / last_price) * 100,2)
            print("percent_change (CP - LP): ", percent_change_last, end=' | ')
        else:
            percent_change_last = 0
        percent_change_open = round(((current_price - open_price) / open_price) * 100,2)
        print("percent_change (CP - OP):", percent_change_open)

        # Insert data into the 'crypto_data' table
        c.execute("INSERT INTO crypto_data VALUES (?,?,?,?,?)", (Time, open_price, current_price, percent_change_last, percent_change_open))
        conn.commit()
        
        last_price = current_price
        time.sleep(300)
except KeyboardInterrupt:
    print("market has been closed")
    # Close the connection to the database
conn.close()

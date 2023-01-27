import yfinance as yf
import time
import sqlite3
from datetime import datetime

#connect to database or create if it doesn't exist
conn = sqlite3.connect('market_data.db')

#create a cursor object to execute SQL commands
cursor = conn.cursor()

#create table
cursor.execute('''CREATE TABLE IF NOT EXISTS market_data
                (time TEXT, open_price REAL, current_price REAL, percent_change REAL)''')

try:
 while True:
  ticker = yf.Ticker("^NSEI")
  data = ticker.history(period="1d")
  open_price = data["Open"].iloc[-1]
  previous_close = data["Close"].iloc[-1]
  current_time = datetime.now().strftime("%H:%M:%S")
  percent_change = (previous_close - open_price) / open_price * 100
  print("Time:",current_time,"Open_Price:",round(open_price,2), "Current_price:",round(previous_close,2),"Overall_change:",round(percent_change,2))
  cursor.execute("INSERT INTO market_data VALUES (?,?,?,?)", (current_time,open_price, previous_close, percent_change))
  conn.commit()
  time.sleep(300)

except KeyboardInterrupt:
    print("market has been closed")

conn.close()

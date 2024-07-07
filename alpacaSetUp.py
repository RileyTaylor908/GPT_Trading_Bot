import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from logger import log_info, save_plot, log_filename

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, api_version='v2')

def fetch_market_data(symbol):
    # 30 days of data from today
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    # Get stock price data
    barset = api.get_bars(
        symbol,
        tradeapi.TimeFrame.Day,
        start=start_date,
        end=end_date,
        feed='iex'  # Use IEX feed
    ).df
    barset.index = barset.index.tz_convert(None)  # Convert to naive datetime if needed

    # Reset index to make 'timestamp' a column
    barset.reset_index(inplace=True)
    
    return barset

def plot_market_data(bars, symbol):
    # Plot stock price data in a graph
    plot = bars.plot(x="timestamp", y="close", legend=False, title=f"{symbol} Closing Prices")
    plot.set_xlabel("Date")
    plot.set_ylabel("Close Price ($)")
    save_plot(plt, log_filename)
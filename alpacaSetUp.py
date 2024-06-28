# data_fetcher.py
import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL, api_version='v2')

def fetch_market_data(symbol):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
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
    # Plot stock price data
    plot = bars.plot(x="timestamp", y="close", legend=False, title=f"{symbol} Closing Prices")
    plot.set_xlabel("Date")
    plot.set_ylabel("Close Price ($)")
    plt.show()

# Example usage
if __name__ == "__main__":
    market_data = fetch_market_data('AAPL')
    plot_market_data(market_data, 'AAPL')
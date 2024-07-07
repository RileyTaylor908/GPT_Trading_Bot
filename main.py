from alpacaSetUp import fetch_market_data, plot_market_data
from gptSetUp import get_market_prediction
from dataPrep import prepare_data_for_gpt
from trade import execute_trade
from logger import log_info

def run_trading_bot():
    log_info("Fetching market data...")
    market_data = fetch_market_data('AAPL')
    log_info("Market data fetched.")
    plot_market_data(market_data, 'AAPL')
    
    log_info("Preparing data for GPT-4...")
    prepared_data = prepare_data_for_gpt(market_data)
    log_info("Getting market prediction from GPT-4...")
    prediction = get_market_prediction(prepared_data)
    log_info(f"Prediction: {prediction}")
    
    log_info("Executing trade based on prediction...")
    trade_details = execute_trade('AAPL', prediction)
    log_info("Trade details: {}".format(trade_details))
    
    if trade_details["action"] == "hold":
        log_info("No trade executed.")
    else:
        log_info(f"Executed {trade_details['action']} trade for {trade_details['quantity']} shares of {trade_details['symbol']}.")
    
if __name__ == "__main__":
    import sys
    from scheduler import run_bot_now, schedule_trading_bot
    
    if len(sys.argv) > 1 and sys.argv[1] == "now":
        run_bot_now()
    else:
        schedule_trading_bot()
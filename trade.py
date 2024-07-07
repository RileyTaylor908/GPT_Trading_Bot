from alpacaSetUp import api

def execute_trade(symbol, prediction):
    # Trade details for logging
    trade_details = {
        "action": "hold",
        "symbol": symbol,
        "quantity": 0
    }
    
    if "prediction: " in prediction.lower():
        action = prediction.lower().split("prediction: ")[1].split()[0].strip()
        
        # Execute trade based on GPT prediction
        # Uses Alpaca API to make paper trades
        if action == "buy":
            # Buy logic
            order = api.submit_order(
                symbol=symbol,
                qty=1,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            trade_details = {
                "action": "buy",
                "symbol": symbol,
                "quantity": 1,
                "order": order
            }
        elif action == "sell":
            # Sell logic
            order = api.submit_order(
                symbol=symbol,
                qty=1,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            trade_details = {
                "action": "sell",
                "symbol": symbol,
                "quantity": 1,
                "order": order
            }
        elif action == "hold":
            # Hold logic (No trade executed)
            trade_details = {
                "action": "hold",
                "symbol": symbol,
                "quantity": 0
            }
    
    return trade_details

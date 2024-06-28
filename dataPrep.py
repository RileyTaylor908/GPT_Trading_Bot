# data_preparer.py
def prepare_data_for_gpt(market_data):
    data_str = market_data.to_string()
    return data_str
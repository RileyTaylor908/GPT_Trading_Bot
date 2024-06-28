# predictor.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_market_prediction(prepared_data):
    messages = [
        {"role": "system", "content": "You are a financial market expert who analyzes market trends."},
        {"role": "user", "content": f"Given the following market data for the last 30 days, predict the next day's market trend:\n{prepared_data} Simply respond with buy, sell, or hold and explain your reasoning for why. Always start with saying 'Prediction: ' and then provide your prediction"}
    ]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()
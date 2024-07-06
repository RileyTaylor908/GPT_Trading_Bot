import schedule
import time
from main import run_trading_bot

def run_bot_now():
    run_trading_bot()

def schedule_trading_bot():
    # Schedule the bot to run daily at market close
    schedule.every().day.at("16:00").do(run_trading_bot)

    while True:
        schedule.run_pending()
        time.sleep(1)
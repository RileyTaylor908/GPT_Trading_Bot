# GPT_Trading_Bot
Gives GPT-4o stock data from Alpaca in order to make trades.

### How to run
1. Open a terminal
2. Create virtual enviroment:
     python3 -m venv myenv
3. Activate virtual enviroment
     .myenv\Scripts\activate (windows)
     source myenv/bin/acivate (mac)
4. Install required packages:
     pip install -r requirement.txt
5. Run main:
     python3 main.py now (to run immediatly)
     python3 main.py (to run scheduled time)

### Config Note
To run this code you also need to create a config.py.
This is how it should look, replace with your api keys:

     ALPACA_API_KEY = ''
     ALPACA_SECRET_KEY = ''
     BASE_URL = ''
     OPENAI_API_KEY = ''


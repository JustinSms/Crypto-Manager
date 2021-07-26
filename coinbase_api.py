import requests
import json
import pandas as pd


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'EUR',
  
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '46df04aa-3464-4382-8f03-3ed068358111',
}


def call_api():
  """call the api and return a df containing the coin symbol, price and timestamp"""
  information_coins_list = []

  json = requests.get(url=url, params=parameters, headers=headers).json()
  coins = json["data"]

  for coin in coins:
    information_coins_list.append([coin["symbol"], coin["quote"]["EUR"]["price"], coin["quote"]["EUR"]["last_updated"]])

  coin_df = pd.DataFrame(information_coins_list, columns=["Symbol","Price","Last_updated"])
  coin_df.set_index("Symbol", inplace=True)
  coin_df["Last_updated"] = pd.to_datetime(coin_df["Last_updated"])

  return coin_df

    
#call_api()

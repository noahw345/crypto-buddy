from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json
import requests
import time
import schedule

#crypto constants 
crypto_assets = {'BTC': 322, 'ETH': 442}

#ifttt URL
ifttt_url_price_change_alert = 'ifttt applet webhook link here'

#coin market cap api and parameters
cp_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'API url here',
}

#connect to coin market cap api
session = Session()
session.headers.update(headers)

#returns information about specificed cryptocurrency 
def get_info(data, coin, value):
    return float(format(data['data'][coin]['quote']['USD'][value], '.2f'))

    #checks if enough change in price has occured to send an alert
def check_price_change(coin):
  response = session.get(cp_api_url, params=parameters)
  data = json.loads(response.text)
  change = get_info(data, coin, 'percent_change_1h')
  #print(f"{datetime.now()}: {change}")
  if change > 5.0:
    make_change_post(crypto_assets.keys()[coin], 'has increased by', change)
  elif change < -5.0:
    make_change_post(crypto_assets.keys()[coin], 'has decreased by', change)
  
#makes a price alert to ifttt
def make_change_post(coin, message, percent_change):
  try:
      json_data = {
        'value1': coin,
        'value2': message,
        'value3': percent_change
        }
      print(json_data)
      #requests.post(ifttt_url_price_change_alert, json=json_data)  
  except(ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

#print(crypto_assets['BTC'])
check_price_change(0)
check_price_change(1)
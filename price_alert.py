#!Library/Frameworks/Python.framework/Versions/3.8/bin/python3 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json
import requests
import time
import schedule

#crypto constants 
crypto_assets = {'BTC': 0, 'ETH': 1}

#ifttt URL
ifttt_url_price_alert = 'ifttt url here'

#coin market cap api and parameters
cp_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'CoinMarketCap API key here'
}

#connect to coin market cap api
session = Session()
session.headers.update(headers)

#returns information about specificed cryptocurrency 
def get_info(data, coin, value):
    return format(data['data'][crypto_assets[coin]]['quote']['USD'][value], '.2f')

#makes scheduled price post to ifttt    
def make_price_post():
  try:
      response = session.get(cp_api_url, params=parameters)
      data = json.loads(response.text)
      json_data = {
        'value1': get_info(data, list(crypto_assets.keys())[1], 'price'),
        'value2': get_info(data, list(crypto_assets.keys())[0], 'price')
        }
      print(json_data)
      requests.post(ifttt_url_price_alert, json=json_data)  
  except(ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

make_price_post()






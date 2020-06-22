# crypto-buddy
Python scripts that serves two functions using the CoinMarketCap API and IFTTT. <br />
First, a notification is sent to a phone at specified times throughout the day <br />
containing the current price of any cryptocurrencies available on CoinMarketCap <br />
(Ex: "ETH: $234.33 BTC: $9547.33). Second, a script monitors the hourly percent change <br />
of any specified crypto-currencies and pushes a notification if a coin changes <br />
by more than 5% in one hour (Ex: "BTC has decreased by 6.3% in the last hour"). <br />
I used crontab to configure price alert to in the morning, afternoon, and evening, and <br />
check change to run hourly. 

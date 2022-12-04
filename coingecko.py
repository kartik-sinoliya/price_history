import requests

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
response = requests.get(url)
price_data_list = response.json()
for price_data in price_data_list:
    print(price_data['symbol'], price_data['current_price'])
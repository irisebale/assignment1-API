import requests 

x = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

print('Current price of Bitcoin is = ' + x.json()['bpi']['USD']['rate'])
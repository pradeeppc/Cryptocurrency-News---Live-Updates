from django.shortcuts import render

def home(resquest):
	import requests
	import json

	
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=IND,USD,EUR")
	price = json.loads(price_request.content)

	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(resquest, 'home.html', {'api': api , 'price': price})

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=IND")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})


	else:
		notfound = "Enter a crypto currency code for eg. BTC for bitcoin currency"
		return render(request, 'prices.html', {'notfound': notfound})
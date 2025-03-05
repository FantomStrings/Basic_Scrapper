import requests

url = "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=.GSPD%7C.GSPS%7C.GSPE%7C.GSPF%7C.GSPHC%7C.GSPI%7C.GSPM%7C.SPLRCR%7C.GSPT%7C.GSPTS%7C.GSPU&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
data = response.json()

# Corrected key path
for stock in data['FormattedQuoteResult']['FormattedQuote']:
    print(f" Name: {stock.get('name', 'N/A')}, Last Price: {stock.get('last', 'N/A')}")


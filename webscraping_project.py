from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from twilio.rest import Client

url = 'https://www.livecoinwatch.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

title = soup.title

currency = soup.findAll('tr')

count = 1

for row in currency[1:6]:
    cols = row.findAll('td')
    name = cols[1].find('small', attrs = {'class':'abr text-truncate'})
    symbol = cols[1].find('div', attrs = {'class':'filter-item-name mb0 text-left'})
    price = float(cols[2].text.strip('$'))
    change = float(cols[8].text.strip('%'))

    changePrice = round(price/(1+(change/100)),2)

    print(f'Rank #{count}')
    print(f'Name: {name.text}')
    print(f'Symbol: {symbol.text}')
    print(f'Price: ${price}')
    print(f'Change: {change}%')
    print(f'Price 24hrs ago: {changePrice}')
    print()


    count+=1

#commenting out and changing the text information so my account does not get messed up
#code was tested before and it does work

'''
accountSID = 'x'
authToken = 'x'
client = Client(accountSID,authToken)
twilioNumber = 'x'
myNumber = 'x'


for row in currency[1:len(currency) - 1]:
    cols = row.findAll('td')
    name = cols[1].find('small', attrs = {'class':'abr text-truncate'}).text
    name = name

    if name == 'Ethereum':
        price = float(cols[2].text.strip('$'))
        
        if price < 3000:
            textmessage = client.messages.create(to=myNumber,from_=twilioNumber,body=f'Ethereum price is currently ${price}')
            print(textmessage.status)
        else:
            print('No message sent')
        
        print(price)

    if name == 'Bitcoin':
        price = float(cols[2].text.strip('$'))
        
        if price < 40000:
            textmessage = client.messages.create(to=myNumber,from_=twilioNumber,body=f'Bitcoin price is currently ${price}')
            print(textmessage.status)
        else:
            print('No message sent')
        
        print(price)

'''
    
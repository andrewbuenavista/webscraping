# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

highestDeath = 0
highestDeathName = ''

lowestDeathRate = 0
lowestDeathName = ''

count = 0

highestTest = 0
highestTestName = ''

lowestTest = 0
lowestTestName = ''

for row in table_rows[2:51]:

    count +=1
    td = row.findAll("td")

    state = td[1].text
    total_cases = int(td[2].text.replace(',',''))
    total_deaths = int(td[4].text.replace(',',''))
    total_tested = int(td[10].text.replace(',',''))

    deathRatio = total_deaths/total_cases
    testRatio = total_cases/total_tested

    if count == 1:
        lowestTest = testRatio
        lowestDeathRate = deathRatio
        lowestDeathName = state

    if deathRatio < lowestDeathRate:
        lowestDeathRate = deathRatio
        lowestDeathName = state

    if deathRatio > highestDeath:
        highestDeath = deathRatio
        highestDeathName = state

    if testRatio < lowestTest:
        lowestTest = testRatio
        lowestTestName = state

    if testRatio > highestTest:
        highestTest = testRatio
        highestTestName = state

print(f"Highest death ratio: {highestDeathName}")
print(f"Lowest death rate: {lowestDeathName}")
print(f"Highest test ratio: {highestTestName}")
print(f"Lowest test ratio: {lowestTestName}")

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


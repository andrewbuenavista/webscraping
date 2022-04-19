
from msilib.schema import tables
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title


movie_table = soup.find('table')
table_rows = movie_table.findAll('tr')


print(title.text)

wb = xl.Workbook()

mySheet = wb.active

bigFont = Font(name='Times New Roman',size=16,bold=True)

mySheet['A1'] = 'No.'
mySheet['B1'] = 'Movie Title'
mySheet['C1'] = 'Release Date'
mySheet['D1'] = 'Gross'
mySheet['E1'] = 'Total Gross'
mySheet['F1'] = '% of Total Gross'

mySheet.column_dimensions['A'].width = 5
mySheet.column_dimensions['B'].width = 30
mySheet.column_dimensions['C'].width = 30
mySheet.column_dimensions['D'].width = 30
mySheet.column_dimensions['E'].width = 30
mySheet.column_dimensions['F'].width = 30

for cell in mySheet["1:1"]:
    cell.font = bigFont
mySheet.title = 'Box Office Report'

count = 2
for row in table_rows[1:6]:

    td = row.findAll('td')
    ranking = td[0].text
    title = td[1].text
    gross = int(td[5].text.replace(',','').replace('$',''))
    total_gross = int(td[7].text.replace(',','').replace('$',''))
    release_date = td[8].text

    percent_gross = round(gross/total_gross * 100,2)

    mySheet['A'+str(count)] = ranking
    mySheet['B'+str(count)] = title
    mySheet['C'+str(count)] = release_date
    mySheet['D'+str(count)] = gross
    mySheet['E'+str(count)] = total_gross
    mySheet['F'+str(count)] = str(percent_gross) + '%'

    count += 1





wb.save('BoxOfficeReport.xlsx')

##
##
##
##


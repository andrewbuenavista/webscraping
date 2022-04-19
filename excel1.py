import openpyxl as xl
from openpyxl.styles import Font

#create a new excel document

wb = xl.Workbook()

mySheet = wb.active

mySheet.title = 'First Sheet'


#create new worksheet
wb.create_sheet(index=1,title='Second Sheet')

mySheet['A1'] = 'An Example of Sum Formula'

#change the font size and italicize

mySheet['A1'].font = Font(name='Times New Roman',size=24, italic=True,bold=True)

#alternatively you can create a font object and assign it

fontObject = Font(name = 'Times New Roman',size = 24, italic = True,bold = True)

mySheet['A1'].font = fontObject

#adding values to cells
mySheet['B2'] = 50
mySheet['B3'] = 75
mySheet['B4'] = 100

mySheet['A5'] = 'Total'
mySheet['A5'].font = Font(size = 16,bold=True)

mySheet['B5'] = '=Sum(B2:B7)'

mySheet.column_dimensions['A'].width = 25

wb.save('PythonToExcel.xlsx')

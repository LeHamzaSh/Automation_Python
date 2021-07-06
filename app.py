import openpyxl as xl
workbook = xl.load_workbook('transactions.xlsx')
sheet = workbook['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1,1)

for row in range(1, sheet.max_row + 1):
     print(row)
import openpyxl as xl
import os
os.chdir(r'C:\Users\Aindriu\Documents\CodeWithMosh\Python Excel Automation')
wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1,1)
print(cell.value)


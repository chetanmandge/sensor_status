from openpyxl import Workbook
import xlsxwriter
import os
# workbook = xlsxwriter.Workbook('LOG.xlsx')
# worksheet = workbook.add_worksheet()
global worksheet
global workbook
PATH = 'H:\Chetan\python\sensor_status\LOG.xlsx'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("File exists and is readable")
    # last_empty_row = len(list(sheet.rows))
    # print(last_empty_row)

    # rows= [16,2,25,8,89,87,87,55,253]

    # worksheet.write_row(last_empty_row+1,1,rows)
else:
    # global worksheet
    # global workbook
    workbook = xlsxwriter.Workbook('LOG.xlsx')
    worksheet = workbook.add_worksheet()
    print("Either the file is missing or not readable")



Workbook.close()
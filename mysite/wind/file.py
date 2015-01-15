import xlrd
def excel_table():
    data=xlrd.open_workbook('weather.xls')
    table=data.sheet_by_name(u'sheet1')
    list1=[]
    list2=[]
    print table.nrows
    for row_index in range(table.nrows):
        contain=table.cell(row_index,0).value
        list1.append(contain)
    return list1
    

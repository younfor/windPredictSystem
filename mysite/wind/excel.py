import xlrd

class excel_table(object):
    list1=[]
    list2=[]
    #def __init__(self):
    def __init__(self,filepath,sheet):
        #data=xlrd.open_workbook('weather.xls')
        data=xlrd.open_workbook(filepath)
       # table=data.sheet_by_name(u'sheet1')
        table=data.sheet_by_name(sheet)
        for row_index in range(table.nrows):
            contain=table.cell(row_index,0).value
            self.list1.append(contain)

        for row_index in range(table.nrows):
            contain=table.cell(row_index,1).value
            self.list2.append(contain)

    def get_list1(self):    
        return self.list1
 
    def get_list2(self):
         return self.list2
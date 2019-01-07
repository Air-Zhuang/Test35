# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 16:08'

'''
excel:office2007之前 xls
'''

import xlrd,xlwt
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\demo.xls"

#读
book=xlrd.open_workbook(path)   #得到book
book.sheets()       #得到sheet
sheet=book.sheet_by_index(0)  #得到sheet

sheet.nrows #列数
sheet.ncols #行数

cell=sheet.cell(0,0) #单元格
print(cell.value)

sheet.row(1) #获取一整行
sheet.row_values(1) #获取一整行的值
sheet.col(1) #获取一整列

sheet.put_cell() #添加一个单元格
#写
wbook=xlwt.Workbook()
wsheet=wbook.add_sheet('sheet1') #添加sheet
wsheet.write() #写单元格
wbook.save(path)    #保存

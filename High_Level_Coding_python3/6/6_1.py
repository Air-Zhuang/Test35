# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 23:31'

'''
读写csv数据
'''

import os
import csv
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\file.csv"

with open(path,'rb') as f:
    reader=csv.reader(f)        #csv读
    for row in reader:
        print(row)

with open(path,'ab') as ff:
    writer=csv.writer(ff)       #csv写
    writer.writerow(['g','s','3','2','a'])
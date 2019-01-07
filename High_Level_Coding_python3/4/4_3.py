'''
如何调整字符串中文本的格式
'''

import os,re
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log=open(path+"\\test\\4_3.txt").read()     #read()读取全部内容
print(log)
print()

#使用re.sub()修改格式
print(re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log))
print()
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log))


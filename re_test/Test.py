'''
.               匹配任意字符（除了\n）
[]              匹配字符集   [abc123] [0-9] [A-Z] [a-z] [0-9a-z]
[^ ]            非
\d / \D         匹配数字\非数字
\s / \S         空格\非空白字符
\w / \W         匹配单词字符[a-zA-Z0-9]/非单词字符
\b / \B
[\u4E00-\u9FA5] 汉字
*               匹配前一个字符0次或者无限次
+               匹配前一个字符1次或者无限次
?               匹配前一个字符0次或者1次
{m}/{m,n}       匹配前一个字符m次或者m次到n次
*?/*?/??        匹配模式变为非贪婪（尽可能少匹配字符）
^               匹配字符串开头
$               匹配字符串结尾
\A / \Z         指定的字符串匹配必须出现在开头/结尾
|               匹配左右任意一个表达式
(ab)            括号中表达式作为一个分组
\<number>       引用编号为num的分组匹配到的字符串
(?P<name>)      分组起一个别名
(?P=name)       引用别名为name的分组匹配字符串
'''

import re

str2='c++=100,java=90,python=80'
info2=re.findall(r'\d+',str2)       #findall：返回列表
print(info2)
info2=re.finditer(r'\d+',str2)      #finditer：返回可迭代对象
print([i.group() for i in info2])
info2=re.search(r'\d+',str2)        #search：直到找到一个匹配的对象
print(info2)
info2=re.match(r'\d+',str2)         #match：第一个字符匹配不上直接返回None
print(info2)
ma=re.fullmatch(r'abc','abc')       #fullmatch：字符串前后必须全部匹配才可以
print(ma.group())

str1="boooooobby123"
regex=".*?(b.*?b)(.*)"
ma=re.match(regex,str1)
print(ma.group(1))
print(ma.group(2))
print()

ma=re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>')
print(ma.group())
print()

str1='imooc videonum=1000'
info=re.search(r'\d+',str1)
print(info.group())
print()


str3='imooc videonum=1000'  #替换
info3=re.sub(r'\d+','1001',str3)
print(info3)
print()

def add1(match):
    val=match.group()
    num=int(val)+1
    return str(num)
info4=re.sub(r'\d+',add1,str3)
print(info4)
print()

str4='imooc:C C++ Java Python,C#'
print(re.split(r':| |,',str4))   #|分割符（中间有空格）
print()

s4='\tabc\t123\txyz\ropq\r'
print(re.sub(r'[\t\r]','',s4))
print()

str5='''
2016-05-25 10:56:23 ashdsjfhgdsajhfdsaf
2016-06-26 11:55:23 shfdjahgsdjfhasdkjfasdf
2017-04-56 05:12:03 aksdjfhaksbjhabsj
'''
print(re.sub('(\d{4})-(\d{2}-(\d{2}))',r'\2/\3/\1',str5))
print(re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',str5))

txt2=re.split('\w+',str5)
print(txt2)
txt3=re.split('\W+',str5)
print(txt3)
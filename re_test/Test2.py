import re

__author__ = 'GitHub:Air-Zhuang'

# print(re.findall(r'^1[38]\d{9}','18345678900'))

# print(re.findall(r'.+(\$.{2})','aaa$bbb'))

# ma=re.match(r'\w+@\w+\.(com|cn)','abc@123.com')
# print(ma.group())

# www='https://www.magicshop.top'
# ma=re.match(r'^(?P<head>http|https)://www\..+?\.(?P<tell>com|cn|top)$',www)
# print(ma.group())
#
# print(re.sub(r'^(?P<head>http|https)://www\..+?\.(?P<tell>com|cn|top)$',r'\g<tell>.magicshop.\g<head>',www))

# ma=re.match(r'^(1|3)\d{16}(\d|x|X)$','370203199506067910')
# print(ma.group())

# pattern=r'abc'
# s='sssabcsss'
# l=re.findall(pattern,s)
# print(l)

ma=re.fullmatch(r'abc','abc')
print(ma.group())
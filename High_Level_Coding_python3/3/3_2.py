'''
实现可迭代对象和迭代器对象
'''
import requests
from collections import Iterable,Iterator

def getWeather(city):
    r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
    data=r.json()['data']['forecast'][0]
    return '%s:%s,%s' % (city,data['low'],data['high'])
print(getWeather(u'北京'))
print(getWeather(u'长春'))
print()

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return city,data['high'],data['low']
    def __next__(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    def __iter__(self):
        return WeatherIterator(self.cities)

city=['北京','上海','广州','长春','青岛','济南','乌鲁木齐','海口','大连','大理','九江','石家庄']

wea=WeatherIterable(city)   #也可以直接迭代WeatherIterator，但是这样只能迭代一次，迭代器就消耗尽了
for i in wea:
    print(i)
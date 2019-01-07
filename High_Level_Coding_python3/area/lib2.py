# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 22:57'

class Triangle(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def getArea(self):
        a,b,c=self.a,self.b,self.c
        p=(a+b+c)/2
        area=(p*(p-a)*(p-b)*(p-c))**0.5
        return area
# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 23:00'

class Rectangle(object):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def get_area(self):
        return self.w*self.h
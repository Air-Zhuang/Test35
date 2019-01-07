# -*- coding: UTF-8 -*-

class Fa:
    '''I'm father'''
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def changeA(self,a):
        self.a=a
    def changeB(self,b):
        self.b=b
    def showFa(self):
        print(self.a)
        print(self.b)
    @staticmethod
    def showSomething():
        print("something")
    @classmethod
    def showSomething2(cls):
        print("something2",cls.__name__)
    def showSomething3(self):
        print("something3")
class Ch(Fa):
    '''I'm child'''
    def __init__(self,a,b,c,d):
        super(Ch,self).__init__(a,b)
        self.c=c
        self.d=d
    def changeC(self,c):
        self.c=c
    def showCh(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
    def __repr__(self):
        return "__repr__啊啊"
if __name__ == '__main__':
    ch=Ch(1,2,3,4)
    ch.showCh()
    print(ch.__dict__)
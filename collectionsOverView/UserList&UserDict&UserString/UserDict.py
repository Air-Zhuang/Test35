import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*2)

dd=DoppelDict2(one=1)
print(dd)
dd['two']=2
print(dd)
dd.update(three=3)
print(dd)
print()

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42
ad=AnswerDict2(a='foo')
print(ad['a'])
d={}
d.update(ad)
d['a']=43
print(d)
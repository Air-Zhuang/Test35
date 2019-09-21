import random

class PickOne(object):
    def __init__(self,item):
        self.item=list(item)
        random.shuffle(self.item)
    def pick(self):
        try:
            print(self.item.pop())
        except Exception as e:
            print("error")
    def __call__(self,name):
        print(name)
        return self.pick()

p=PickOne(range(10))
p.pick()
p("air")
print(callable(p.pick))
print(callable(p))
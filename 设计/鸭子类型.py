class Person(object):
    def voice(self):
        print("人gua gua")

class Duck(object):
    def voice(self):
        print("鸭子gua gua")

def xxx(animal):
    animal.voice()

if __name__ == '__main__':
    p=Person()
    d=Duck()
    xxx(p)
    xxx(d)
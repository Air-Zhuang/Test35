"""工厂模式：解决对象创建问题"""
class DogToy:
    def speak(self):
        print("wang wang")

class CatToy:
    def speak(self):
        print("miao miao")

def toy_factory(toy_type):
    if toy_type=='dog':
        return DogToy()     #返回的是实例
    elif toy_type=='cat':
        return CatToy()
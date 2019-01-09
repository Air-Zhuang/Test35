'''
mro算法概括：
    如果是菱形继承则使用广度优先算法，
    如果是非菱形继承则使用深度优先算法
'''

'''super的调用顺序实际是mro算法'''
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

d=D()
print(D.__mro__)
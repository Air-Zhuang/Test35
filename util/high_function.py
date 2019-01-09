#函数存储在列表中调用
def a_this(x):
    return x+1
def b_this(x):
    return x+2
def c_this(x):
    return x+3

# l=[a_this,b_this,c_this] #用法相同
l=[globals()[name] for name in globals() if name.endswith("_this")]
print(l)

def best(num):
    print(max(i(num) for i in l))

best(7)

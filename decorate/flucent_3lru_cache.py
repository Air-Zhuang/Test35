from Test35.decorate.flucent_2wraps import clock2
import functools

@clock2
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(6))

'''functools.lru_cache装饰器实现了备忘功能，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算'''
'''functools.lru_cache(maxsize=128,typed=False)'''
'''maxsize参数制定存储多少个调用结果。缓存满了之后，旧的结果会被扔掉，maxsize应设为2的幂。
    typed参数如果设为True，把不同参数类型得到的结果分开保存。
    被lru_cache装饰的函数，它的所有参数都必须是可散列的'''
@functools.lru_cache()
@clock2
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(6))
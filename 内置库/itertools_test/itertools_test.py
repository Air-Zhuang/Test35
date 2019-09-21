'''zip_longest,islice,repeate,count,takewhile,cycle,chain,chain.from_iterable,compress,
    dropwhile,filterfalse,accumulate,starmap,product,combinations,combinations_with_replacement,
    permutations,groupby,tee'''

'''itertools.zip_longest'''
'''使用可选的fillvalue(默认值为None)填充缺失的值,因此可以继续产出，直到最长的可迭代对象耗尽'''
import itertools
print('itertools.zip_longest------------------:')
print(list(itertools.zip_longest(range(3),'ABC',[0.0,1.1,2.2,3.3],fillvalue=-1)))
print()

'''itertools.islice'''
'''返回迭代器，其中的项目来自　将seq，从start开始,到stop结束，以step步长切割后'''
print('itertools.islice------------------:')
listone = ['a','b','c']
listtwo = ['11','22','abc']
listthree = listone + listtwo
for item in itertools.islice(listthree,3,5):
    print(item, end=" ")
print();print()

'''itertools.repeate'''
print('itertools.repeate------------------:')
listone = ['a','b','c']
for item in itertools.repeat(listone,3):
    print(item, end=" ")
print();print()

'''itertools.count'''
'''功能：从100开始数10个数，cout返回一个无界的迭代器
输出：100 101 102 103 104 105 106 107 108 109 110'''
print('itertools.count------------------:')
i = 0
for item in itertools.count(100):
    if i>10:
        break
    print(item,end=" ")
    i = i+1
print();print()

'''itertools.takewhile'''
'''itertools.takewhile会生成一个使用另一个生成器的生成器，在指定的条件计算结果为False时停止'''
print('itertools.takewhile------------------:')
gen=itertools.takewhile(lambda n:n<3,itertools.count(1,0.5))
print(list(gen))
print()

'''itertools.dropwhile(predicate,it)'''
'''处理it,跳过predicate的计算结果为真值的元素，然后产出剩下的各个元素(不再进一步检查)
    不再进一步检查，意味着遇到False,开始后面的都返回'''
print('itertools.dropwhile------------------:')
def vowel(c):
    return c.lower() in 'aeiou'
print(list(itertools.dropwhile(vowel,'Aardvark')))
print()

'''itertools.cycle'''
'''从列表中取元素，到列表尾后再从头取...
无限循环，因为cycle生成的是一个无界的失代器'''
print('itertools.cycle------------------:')
listone = ['a', 'b', 'c']
i = 0
for item in itertools.cycle(listone):
    i+=1
    print(item,end=" ")
    if i==10:
        break
print();print()

'''itertools.chain'''
'''生成列表迭代器'''
print('itertools.chain------------------:')
# listone = ['a','b','c']
listone = 'a'
listtwo = ['11','22','abc']
for item in itertools.chain(listone,listtwo):
    print(item,end=" ")
print();print()

l=[['abc'],[12],["fff"],["567"]]
print(list(itertools.chain(*l)))
d=[{'abc':111},{12:222},{"fff":333},{"567":444},{"567":444}]
print(list(itertools.chain(*d)))
print()

'''itertools.chain.from_iterable(it)'''
'''产出it生成的各个可迭代对象中的元素，一个接一个，无缝连接在一起；
    it应该产出可迭代的元素，例如可迭代的对象列表'''
print('itertools.chain.from_iterable------------------:')
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
d2=[(1,'A'),(2,'B'),(3,'C')]
print(list(itertools.chain.from_iterable(d2)))
print()

'''itertools.compress(it,selector_it)'''
'''并行处理两个可迭代的对象;如果selector_it中的元素是真值，产出it中对应的元素'''
print('itertools.compress------------------:')
print(list(itertools.compress('Aardvark',(1,0,1,1,0,1))))
print()

'''itertools.filterfalse(predicate,it)'''
'''与filter相反'''
print('itertools.filterfalse------------------:')
def vowel(c):
    return c.lower() in 'aeiou'
print(list(itertools.filterfalse(vowel,'Aardvark')))
print()

'''itertools.accumulate(it,[func])'''
'''产出累积的总和；如果提供了func，那么把前两个元素传给它，
    然后把计算结果和下一个元素传给它，以此类推，最后产出结果'''
print('itertools.accumulate------------------:')
sample=[5,4,2,8,7,6,3,0,9,1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample,min)))
print(list(itertools.accumulate(sample,max)))
import operator
print(list(itertools.accumulate(sample,operator.mul)))
print(list(itertools.accumulate(range(1,11),operator.mul)))
print()

'''itertools.starmap(func,it)'''
'''把it中的各个元素传给func,产出结果;输入的可迭代对象应该产出可迭代的元素it，
    然后以func(*it)这种形式调用func'''
print('itertools.starmap------------------:')
print(list(itertools.starmap(operator.mul,[(3, 'a'), (4, 'l'), (5, 'b'), (6, 'a'), (7, 't'), (8, 'r'), (9, 'o'), (10, 'z')])))
print(list(itertools.starmap(operator.mul,enumerate('albatroz',3))))
print()

'''itertools.product(it1,...,itN,repeat=1)'''
'''计算笛卡尔积：从输入的各个可迭代对象中获取元素，合并成由N个元素组成的元组，
    与镶嵌的for循环效果一样;repeat指明重复处理多少次输入的可迭代对象'''
print('itertools.product------------------:')
print(list(itertools.product('ABC',range(2))))
suits='spades hearts diamonds clubs'.split()
print(list(itertools.product('AK',suits)))
print(list(itertools.product('ABC')))
print(list(itertools.product('ABC',repeat=2)))
print(list(itertools.product(range(2),repeat=3)))
print(list(itertools.product('AB',range(2),repeat=2)))
print()

'''itertools.combinations(it,out_len)'''
'''把it产出的out_len个元素组合在一起，然后产出
    (在it里选择out_len个元素组成元组，有多少种组法就返回多少种)'''
print('itertools.combinations------------------:')
print(list(itertools.combinations('ABC',2)))
print()

'''itertools.combinations_with_replacement(it,out_len)'''
'''把it产出的out_len个元素组合在一起，然后产出,
    包含相同元素的组合'''
print('itertools.combinations_with_replacement------------------:')
print(list(itertools.combinations_with_replacement('ABC',2)))
print()

'''itertools.permutations(it,out_len=None)'''
'''把out_len个it产出的元素排列在一起，然后产出这些排列;out_len的默认值等于len(list(it))'''
print('itertools.permutations------------------:')
print(list(itertools.permutations('ABC',2)))
print()

'''itertools.groupby(it,key=None)'''
'''产出由两个元素组成的元素，形成为(key,group)，
    其中key是分组标准，group是生成器，用于产出分组里的元素'''
print('itertools.groupby------------------:')
print(list(itertools.groupby('LLLLAAGG')))
for char,group in itertools.groupby('LLLLAAGG'):
    print(char,'->',list(group))

animals=['duck','eagle','rat','giraffe','bear','bat','dolphin','shark','lion']
animals.sort(key=len)
print(animals)
for length,group in itertools.groupby(animals,len):
    print(length,'->',list(group))
print()
for length,group in itertools.groupby(reversed(animals),len):
    print(length, '->', list(group))
print()

'''itertools.tee(it,n=2)'''
'''产出一个由n个生成器组成的元组，每个生成器用于单独产出输入的可迭代对象中的元素'''
print('itertools.tee------------------:')
for i in itertools.tee('ABC'):
    print(list(i))




















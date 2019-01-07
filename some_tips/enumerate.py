'''enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。'''
'''enumerate(sequence, [start=0])'''

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons))) #生成的结果像zip生成的结果
print(list(enumerate(seasons, start=1)))       # 小标从 1 开始

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])
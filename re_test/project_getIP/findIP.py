import re

target='Loopback100'

with open('1.txt','r') as f:
    l=f.readlines()
    # print(l)
    for i in l:
        if target+' is' in i:
            targetline =l.index(i)
            # print(l.index(i))

    for i in range(targetline+1,len(l)):
        # print(l[i])
        ma = re.search(r'address is \d+\.\d+\.\d+\.\d+/\d+', l[i])
        if ma:
            print(ma.group())
        if not l[i].startswith('  '):
            break

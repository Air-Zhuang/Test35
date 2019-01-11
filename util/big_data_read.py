'''
一次性读取指定分割符的超大文件
'''

'''
f       : 文件
newline : 分隔符
size    : 一次性读取多少字符
'''
def myreadlines(f,newline,size=4096):
    buf=""
    while True:
        while newline in buf:
            pos=buf.index(newline)
            yield buf[:pos]
            buf=buf[pos+len(newline):]
        chunk=f.read(size)

        if not chunk:
            #说明已经读到了文件结尾
            yield buf
            break
        buf+=chunk


with open("input.txt") as f:
    for line in myreadlines(f,"{|}",4096*10):
        print(line)     #得到每个分割符出来的内容
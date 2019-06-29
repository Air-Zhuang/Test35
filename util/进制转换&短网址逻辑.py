
'''10进制 -> 2进制'''
def mybin2(num):
    res=[]
    while num:
        num,rem=divmod(num,2)
        res.append(str(rem))
    return ''.join(reversed(res))

print(mybin2(10))

'''10进制 -> 62进制'''
def mybin62(num):
    res=[]
    while num:
        num,rem=divmod(num,62)
        res.append(str(rem))
    return ''.join(reversed(res))

print(mybin62(99999))


CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
'''短网址逻辑:自增id -> 短网址'''
def url_encode(num):
    if num==0:
        return CHARS[0]
    res=[]
    while num:
        num,rem=divmod(num,len(CHARS))  #62
        res.append(CHARS[rem])
    return ''.join(reversed(res))

print(url_encode(99999))    #99999为自增id
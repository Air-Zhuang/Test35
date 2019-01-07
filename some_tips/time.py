'''
>>> time.time()
1534408212.3464816

>>>time.gmtime()
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=8, tm_min=22, tm_sec=22, tm_wday=3, tm_yday=228, tm_isdst=0)

>>> time.asctime()
'Thu Aug 16 16:26:23 2018'

>>> time.mktime((2018,8,16,16,0,0,0,0,0))
1534406400.0

>>> time.localtime(1534406400.0)
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=16, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=228, tm_isdst=0)
'''
import time
print(time.localtime(time.mktime((1995,6,6,0,0,0,0,0,0)))['tm_wday'])
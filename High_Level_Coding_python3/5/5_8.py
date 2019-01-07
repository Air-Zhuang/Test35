# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/30 23:34'

'''
读取yaml文件
'''

import yaml
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\file\\config.yaml"

class Execute_yaml(object):
    def readfile(self,firstPara,secondPara):
        with open(path,'rb') as f:
            return yaml.load(f)[firstPara][secondPara]
    def writefile(self,id,port,bp,deviceName):
        data={
            "user_info_"+str(id):{
                "port":str(port),
                "bp":str(bp),
                "deviceName":str(deviceName)
            }
        }
        with open(path, 'a') as f:
            yaml.dump(data,f)
if __name__ == '__main__':
    e=Execute_yaml()
    e.writefile(1,4724,4801,'aaa')
    print(e.readfile('user_info_1','bp'))
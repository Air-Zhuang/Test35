import gridfs
import pymongo

conn=pymongo.MongoClient('localhost','27017')
db=conn.grid

fs=gridfs.GridFS(db)

files=fs.find()
#分别取每一个文件
for file in files:
    #打印每个文件名称
    print(file.filename)
    if file.filename=='mm.jpg':
        with open(file.filename,'wb') as f:
            #从数据库读取内容
            file.read()
            #写入到本地
            file.write()
conn.close()
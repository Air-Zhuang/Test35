import gridfs
import pymongo

conn=pymongo.MongoClient('localhost','27017')
db=conn.grid

fs=gridfs.GridFS(db)

f=open('mm.jpg','rb')
fs.put(f.read(),filename='mm2.jpg')

conn.close()
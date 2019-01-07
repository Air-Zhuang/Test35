import pymongo

conn=pymongo.MongoClient('localhost',27017)

db=conn.test
myset=db.zzh
'''
insert()
insert_many()
insert_one()
save() 如果有则修改，没有则插入
'''
# myset.insert({"name" : "Frank", "age" : 26, "sex" : "m" })
# myset.insert([{"name" : "Frank", "age" : 26, "sex" : "m" },{"name" : "Frank", "age" : 26, "sex" : "m" }])

'''
查找
myset.find()
myset.find({},{'_id':0})
'''
# cursor=myset.find({},{'_id':0}).skip(1).limit(3)    #cursor不指向开头的话skip.limit.sort会报错
# for i in cursor:
#     print(i)    #i是字典

# cursor=myset.find({'$or':[{'sex':'f'},{'age':{'$gt':20}}]})
# for i in cursor:
#     print(i)

'''
修改
'''
# cursor=myset.update_many({},{'$set':{'hobby':'Java'}})   #全部修改
# cursor=myset.find()
# for i in cursor:
#     print(i)

# cursor = myset.update({}, {'$set': {'hobby': 'pyhon'}}, upsert=True)  #如果匹配文档不存在则插入
# for i in cursor:
#     print(i)

'''
删除
'''
# cursor=myset.delete_one({})
# cursor=myset.delete_many({"name":'Frank'})
# cursor=myset.remove({"name":'Frank'})

'''
复合操作
'''
# print(myset.find_one_and_delete({'name':'Frank'}))      #查找一条name=Frank 并删除一条

'''
索引
'''
# index=myset.create_index('name')                                #正向索引
# index=myset.create_index([('age',-1)])                          #逆向索引
# index=myset.create_index([('name',1),('age',-1)])               #复合索引
# index=myset.create_index('name',name='MyIndex',unique=True)     #唯一索引
# index=myset.create_index('name',sparse=True)                      #稀疏索引


# indexs=myset.list_indexes()
# for i in indexs:
#     print(i)

# myset.drop_index('name_1')                    #删除单个索引
# myset.drop_indexes()                           #删除所有索引

'''
聚合
'''
p=[{'$group':{'_id':'$name','num':{'$sum':1}}},{'$match':{'num':{'$gt':1}}}]
cursor=myset.aggregate(p)
for i in cursor:
    print(i)

conn.close()
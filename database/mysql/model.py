import pymysql

db = pymysql.connect(host="localhost",port=3306,user="root",password="123456",db="MOSHOU",charset="utf8")
cursor = db.cursor()

sql="select * from sanguo;"
try:
    cursor.execute(sql)
except Exception as e:
    db.rollback()
    print("Failed",e)

result=cursor.fetchall()
for id,name,gongji,fangyu,sex,country in result:
    print(id,name,gongji,fangyu,sex,country)

db.commit()

cursor.close()

db.close()

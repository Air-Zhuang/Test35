from collections import namedtuple

User=namedtuple("User",["name","age","height","edu"])
user_tuple=("bobby",29,175)
user_tuple_full=("bobby",29,175,"master")
user_dict={
    "name":"bobby",
    "age":29,
    "height":175
}
#_fields
print(User._fields)
#*args
user1=User(*user_tuple,"master")
#**kw
user2=User(**user_dict,edu="master")
#_make
user3=User._make(user_tuple_full)

print(user1.age,user1.name,user1.height,user1.edu)
print(user2.age,user2.name,user2.height,user2.edu)
print(user3.age,user3.name,user3.height,user3.edu)

#_asdict()
print(user1._asdict())
print(user2._asdict())
print(user3._asdict())
#拆包
name,age,*other=user1
print(name,age,*other)

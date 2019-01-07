from collections import ChainMap

#旧方法
user_dict1={"a":"bobby1","b":"bobby2"}
user_dict2={"c":"bobby2","d":"bobby3"}
for key,value in user_dict1.items():
    print(key,value)
print()
for key,value in user_dict2.items():
    print(key,value)
print()

#ChainMap
user_dict1={"a":"bobby1","b":"bobby2"}
user_dict2={"c":"bobby2","d":"bobby3"}
new_dict=ChainMap(user_dict1,user_dict2)
print("new_dict:",new_dict)
print(isinstance(new_dict,dict))

for key,value in new_dict.items():
    print(key,value)
print()

print(new_dict.maps)
new_dict.maps[0]["a"]="bobby"
print(new_dict.maps)
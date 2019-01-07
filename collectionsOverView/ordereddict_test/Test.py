from collections import OrderedDict

#有序的 python2默认无序 python3默认有序
user_dict=OrderedDict()
user_dict["b"]="bobby2"
user_dict["a"]="bobby1"
user_dict["c"]="bobby3"
print(user_dict)

user_dict.move_to_end("b")
print(user_dict)

print(user_dict.popitem())
print(user_dict.pop("c"))
print(user_dict)
from collections import Counter

#统计
users=["bobby1","bobby2","bobby3","bobby1","bobby2","bobby2"]
user_counter=Counter(users)
user2_counter=Counter("adsfsadadasfdasgadgfsdgf")
print(user_counter)
print(user2_counter)
user2_counter.update("asdfsagdfshgfhdafgasdfdsagf")
print(user2_counter)
#统计最多的两个
print(user_counter.most_common(2))

from collections import deque
import copy
#deque是线程安全的，list不是线程安全的

user_deque=deque(["bobby1","bobby2","bobby3"])
print(user_deque)
user_deque.appendleft("bobby8")
print(user_deque)

#深拷贝
user2_deque=copy.deepcopy(user_deque)
print(user2_deque)

#extend:在原基础上扩容
user_deque.extend(user2_deque)
print(user_deque)

#reverse
user_deque.reverse()
print(user_deque)
import time
import socket


'''==============================================='''
print(time.time())

def _time():
    return 1234

time.time=_time

print(time.time())

'''==============================================='''
print(socket.socket)

print("After monkey patch")

from gevent import monkey
monkey.patch_socket()

print(socket.socket)
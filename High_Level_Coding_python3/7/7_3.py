'''
实现类似with的让对象支持上下文管理
'''

'''
实现上下文管理协议，需定义实例的__enter__,__exit__
方法，他们分别在with开始和结束时被调用
'''

from sys import stdin, stdout
import getpass
import telnetlib
from collections import deque

class TelnetClient:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port 

    def __enter__(self):
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])
        return self                 #这里要返回值

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('IN __exit__', exc_type, exc_value, exc_tb)

        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelines(self.history)

        return True

    def login(self):
        # user
        self.tn.read_until(b"login: ")
        user = input("Enter your remote account: ")
        self.tn.write(user.encode('utf8') + b"\n")

        # password
        self.tn.read_until(b"Password: ")
        password = getpass.getpass()
        self.tn.write(password.encode('utf8') + b"\n")
        out = self.tn.read_until(b'$ ')
        stdout.write(out.decode('utf8'))

    def interact(self):
        while True:
            cmd = stdin.readline()
            if not cmd:
                break

            self.history.append(cmd)
            self.tn.write(cmd.encode('utf8'))
            out = self.tn.read_until(b'$ ').decode('utf8')

            stdout.write(out[len(cmd)+1:])
            stdout.flush()

# client = TelnetClient('192.168.0.105')
# client.connect()
# client.login()
# client.interact()
# client.cleanup()

with TelnetClient('192.168.0.105') as client:
    raise Exception('TEST')
    client.login()
    client.interact()

print('END')


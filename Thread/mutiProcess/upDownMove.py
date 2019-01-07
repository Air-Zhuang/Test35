import multiprocessing as mp
import os


def up():
    with open('upDownMovefile\\1.jpeg', 'rb') as f:
        context = f.read(os.path.getsize('upDownMovefile\\1.jpeg') // 2)
        print(context)
        with open('upDownMovefile\\2.jpeg', 'ab') as f2:
            f2.write(context)

def down():
    with open('upDownMovefile\\1.jpeg', 'rb') as f:
        f.seek(os.path.getsize('upDownMovefile\\1.jpeg') // 2, 0)
        context = f.read()
        print(context)
        with open('upDownMovefile\\2.jpeg', 'ab') as f2:
            f2.seek(os.path.getsize('upDownMovefile\\2.jpeg') // 2)
            f2.write(context)

if __name__ == '__main__':
    p1 = mp.Process(target=up)
    p2 = mp.Process(target=down)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

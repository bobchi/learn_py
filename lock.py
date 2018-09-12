from threading import Thread, Lock
import time


lst = []


def add():
    my_lock.acquire()
    for x in range(0, 5):
      lst.append(x)
      time.sleep(0.1)
    my_lock.release()
    print(lst)


if __name__ == '__main__':
    my_lock = Lock()
    for x in range(0,3):
        t = Thread(target=add)
        t.start()


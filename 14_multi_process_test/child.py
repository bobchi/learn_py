from multiprocessing import Process
from multiprocessing.managers import BaseManager

def add_user1(list):
    list.append('兔兔')

def add_user2(list):
    list.append('胖子')

if __name__ == '__main__':
    bm = BaseManager(address=('127.0.0.1', 8084), authkey=b'12345')
    bm.register('get_user')
    bm.connect()
    my_list = bm.get_user()

    p1 = Process(target=add_user1, args=(my_list,))
    p1.start()

    p2 = Process(target=add_user2, args=(my_list,))
    p2.start()
    print(my_list)

    p1.join()
    p2.join()

    print(my_list)


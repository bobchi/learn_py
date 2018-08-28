from multiprocessing import Process, Manager

def add_user(list):
    list.append('zs')
    print(list)


if __name__ == '__main__':
    m = Manager()
    my = m.list(['tt'])
    p = Process(target=add_user, args=(my,))
    p.start()
    p.join()
    # print(my)


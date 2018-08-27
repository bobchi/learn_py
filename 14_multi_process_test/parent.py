from multiprocessing.managers import BaseManager

if __name__ == "__main__":
    bm = BaseManager(address=('', 8084), authkey=b'12345')
    bm.register('get_user', callable=lambda: ['宝哥哥', '爸爸'])
    bm_server = bm.get_server()
    bm_server.server_forever()


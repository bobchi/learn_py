import os
# f = None
# try:
#     f = open('./files/test.txt', 'r')
#     print(f.read())
# except:
#     print('文件没找到')
# finally:
#     print('finally')
#     if f is not None:
#         f.close()

class FileReader:
    def __init__(self, _path):
        self.path = _path
    def __enter__(self):
        print('__enter__')
        return self
    def print_me(self):
        self.file = open(self.path)
        print(self.file.read())
    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.file.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        if exc_type is None:
            self.file.close()
        return True


with FileReader('./files/test1.txt') as fr:
    fr.print_me()


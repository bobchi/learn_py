import os

data_dir = './htmls'
all_path = os.listdir(data_dir)

# print(all_path)

data_list = []

for p in all_path:
    print(os.path.isfile(os.path.join(data_dir, p)))


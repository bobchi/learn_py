import pandas as pd

user = pd.Series(['bao', 32], index=['name', 'age'])
user2 = pd.Series(['tutu', 2.5], index=['name', 'age'])

users = pd.DataFrame([{"name": "qiu", "age": 10}, {"name": "qiu", "age": 10}])

print(users)


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 余弦相似性
user1 = np.array([2,3,3,2,1,2,4])
user2 = np.array([2,2,3,4,4,5,4])

user = np.array([[118,193,238,230],[118,42,238,230],[58,193,238,230],[118,193,238,99]])
# reshape(1,7)是构建1行7列的向量
# print(user1.reshape(1,7))
# print(cosine_similarity(user1.reshape(1,7), user2.reshape(1,7)))

# 修正的余弦相似性，向量元素减去一个均值，如user1-user1.mean()
user1 = user1-user1.mean()
user2 = user2-user2.mean()
print(cosine_similarity(user1.reshape(1,7), user2.reshape(1, 7)))

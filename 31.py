import jieba
import jieba.analyse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer


# github: https://github.com/fxsjy/jieba
# 引入停用词文档
# jieba.analyse.set_stop_words('./files/stopwords.txt')
# 分词开始
# seg_list = jieba.analyse.extract_tags('据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。')
#
# print(' '.join(seg_list))

# 封装分词函数
def get_words(content):
    word_lst = jieba.cut(content)
    tags = jieba.analyse.extract_tags(content)
    return [item for item in word_lst if item in tags]

# 过滤停用词手工写法
# str1 = '据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。'
# lst = jieba.cut(str, cut_all=False)
# stop = [line.decode('utf-8').strip() for line in open('./files/stopwords.txt', 'rb').readlines()]
# tags = jieba.analyse.set_stop_words('./files/stopwords.txt')
# print(tags)

# 过滤停用词手工写法2
# str1 = '据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。'
# seg_lst = jieba.cut(str1, cut_all=False)
# tags = jieba.analyse.extract_tags(str1)
# # 根据结巴解析出来的分词都列出来，而不合并重复分词
# res = [item for item in seg_lst if item in tags]
# print('/'.join(res))
# print('/'.join(tags))

# 词频计算 词频tf x 逆向文件频率idf = tf-idf 分数
words_list=['程序员 前途 程序员 快递 工作 快递','工作 快递 无聊 快递 ','圣诞节 工作']

# print((2/14)*np.log(3/1))
# print((2/14)*np.log(3/2))

# 使用sklearn得出词频矩阵
cv = CountVectorizer()
# 将词列表加入训练
cv_result = cv.fit_transform(words_list)
# 输出过滤后的词矩阵
print(cv.get_feature_names())
# 输出词出现次数矩阵
print(cv_result.toarray())
# 计算出tfidf
tfidf_trans = TfidfTransformer().fit_transform(cv_result)
print(tfidf_trans.toarray())

# 直接算出tfidf
tv = TfidfVectorizer()
tfidf = tv.fit_transform(words_list)
print(tv.get_feature_names())
print(tfidf.toarray())




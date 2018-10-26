import jieba
import jieba.analyse
# github: https://github.com/fxsjy/jieba
# 引入停用词文档
# jieba.analyse.set_stop_words('./files/stopwords.txt')
# 分词开始
# seg_list = jieba.analyse.extract_tags('据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。')
#
# print(' '.join(seg_list))

# 过滤停用词手工写法
str1 = '据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。'
lst = jieba.cut(str, cut_all=False)
stop = [line.decode('utf-8').strip() for line in open('./files/stopwords.txt', 'rb').readlines()]
tags = jieba.analyse.set_stop_words('./files/stopwords.txt')
print(tags)



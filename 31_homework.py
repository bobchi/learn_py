import jieba
import jieba.analyse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer


def get_words(content):
    word_lst = jieba.cut(content)
    tags = jieba.analyse.extract_tags(content)
    res = [item for item in word_lst if item in tags]
    return ' '.join(res)


if __name__ == '__main__':
    doc1 = "据说程序员是一个很有前途的工作，我要好好学习，将来做程序员。前两天我在网上买了一本开发方面的书，卖家发的顺丰快递，快递小哥2天就给送到，这几天我正式开始写代码学习了。"
    doc2 = "现在我工作了十几年，每天过着同样的生活，送快递、收快递，太无聊了。"
    doc3 = "圣诞节要到了。不要工作了，大家嗨起来了。"

    tv = TfidfVectorizer()
    tfidf_res = tv.fit_transform([get_words(doc1), get_words(doc2), get_words(doc3)])
    print(tv.get_feature_names())
    print(tfidf_res.toarray())

import jieba
import jieba.analyse
import jieba.posseg


file_name = './jieba/test.txt'
topK = 10
content = open(file_name, 'rb').read()

print('---------------------------分词----------------------------')
jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
seg_list = jieba.cut(content,use_paddle=True) # 使用paddle模式
print("Paddle Mode: \n" + '/'.join(list(seg_list)))
seg_list = jieba.cut(content, cut_all=True)
print("Full Mode: \n" + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut(content, cut_all=False)
print("Default Mode: \n" + "/ ".join(seg_list))  # 精确模式
seg_list = jieba.cut_for_search(content)  # 搜索引擎模式
print('搜索引擎模式:')
print(", ".join(seg_list))

print('------------------------自定义词典--------------------------')
print('添加单个词：')
jieba.suggest_freq('王者荣耀', True)
jieba.suggest_freq('超神', True)
words = jieba.cut(content)
print('/'.join(words))

print('使用词典：')
jieba.load_userdict("./jieba/dict.txt")
words = jieba.cut(content)
print('/'.join(words))

print('-------------------------TF-IDF----------------------------')
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))


print('------------------------TextRank---------------------------')
for x, w in jieba.analyse.textrank(content, topK=topK, withWeight=True):
    print('tag: %s\t\t weight: %f' % (x, w))

print('------------------------词性标注---------')
words = jieba.posseg.cut(content)
for word, flag in words:
    print('%s<%s> ' % (word, flag),end = '')
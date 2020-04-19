import jieba
import jieba.analyse


file_name = 'file.txt'
topK = 10

content = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
print('-'*40)
print(' TF-IDF')
print('-'*40)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(content, topK=topK, withWeight=True):
    print('tag: %s\t\t weight: %f' % (x, w))
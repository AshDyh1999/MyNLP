#-*- coding:utf-8 -*-
from snownlp import SnowNLP
s = SnowNLP(u'一次满意的购物体验')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'产品和服务都很好')
print(s.sentences,'\t\t', s.sentiments)  
s = SnowNLP(u'卖家服务态度很好，好评')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'东西不错，但是包装不太好')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'产品质量不行，没几天就坏了')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'店家卖完就不理我了，差评')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'一次很差的购物体验')
print(s.sentences,'\t\t', s.sentiments) 
s = SnowNLP(u'这个商品不给力')
print(s.sentences,'\t\t', s.sentiments)




#对类别标签的文本做词嵌入对应，即  类别文本——>300向量

import pickle as pl
import numpy as np
glove_path=r'G:\wordEmbedding\glove\glove.42B.300d.txt'
with open(glove_path, encoding="utf8") as glove:
    glove = glove.readlines()
embeddings = {}
for line in glove:
    line = line.split()
    word = line[0]
    vector = np.asarray(line[1:], dtype='float32')
    embeddings[word] = vector
#
list= np.zeros((7, 300),dtype=np.float32)                            #70：类别标签的个数   300：向量维度
# list[0]=embeddings['event']
# list[1]=embeddings['concept']
# list[2]=embeddings['sport']
# list[3]=embeddings['work']
# list[4]=embeddings['device']
# list[5]=embeddings['species']
# list[6]=embeddings['agent']
# list[7]=embeddings['place']
# list[8]=embeddings['unit']
# print(list)
# pl.dump(list,open('label_vector_level1','wb'))

def compute_embeddings(label):
    print(label)
    words=label.split()
    print(words)
    emb=np.zeros(300,dtype=np.float32)
    for word in words:
        emb=np.add(emb,embeddings[word])
    print(emb)
    return emb

with open('../DATA/WOS46985/label1.txt',encoding='utf-8') as f:                                 #修改路径
    f=f.readlines()
for i,label in enumerate(f):
    list[i]=compute_embeddings(label)
print(list.shape)
pl.dump(list,open('../DATA/WOS46985/label_1_vector','wb'))





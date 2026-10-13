import re
import math
import sys
from src.lib.text import normalize,tokenize,count_freq,top_n
a=[]
a.append(input())
k=10
print(a)
print("Всего слов:",len(tokenize(normalize(a))[0]))
print("Уникальных слов:",len(set(tokenize(normalize(a))[0])))
print("Топ-5: ")
print("слово"+" "*(k-len("слово"))+"|"*(math.ceil(k/1000))+" частота")
if k>0:
    print("-"*k*2)
print(top_n(count_freq(tokenize(normalize(a))[0]),5))
for i in range(len(set(tokenize(normalize(a))[0]))):
    print(top_n(count_freq(tokenize(normalize(a))[0]),5)[i][1]+" "*(k-len(top_n(count_freq(tokenize(normalize(a))[0]),5)[i][1]))+\
          "|"*(math.ceil(k/1000))+" "+str(top_n(count_freq(tokenize(normalize(a))[0]),5)[i][0]))
#запуск       "Привет, мир! Привет!!!" | python -m src.lab03.text_stats


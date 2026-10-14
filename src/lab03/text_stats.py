import re
import math
import sys
from src.lib.text import normalize,tokenize,count_freq,top_n
a=input()
#a.append(input())
k=10
print("Всего слов:",len(tokenize(normalize(a))))
print("Уникальных слов:",len(set(tokenize(normalize(a)))))
print("Топ-5: ")
print("слово"+" "*(k-len("слово"))+"|"*(math.ceil(k/1000))+" частота")
if k>0:
    print("-"*k*2)
for i in range(len(set(tokenize(normalize(a))))):
    print(top_n(count_freq(tokenize(normalize(a))),5)[i][0]+" "*(k-len(top_n(count_freq(tokenize(normalize(a))),5)[i][0]))+\
          "|"*(math.ceil(k/1000))+" "+str(top_n(count_freq(tokenize(normalize(a))),5)[i][1]))
#запуск       Привет, мир! Привет!!!  | python -m src.lab03.text_stats


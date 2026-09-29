import re
from textA import*
a=["Привет, мир! Привет!!!"]
k=10
print(a)
print("Всего слов:",len(tokenize(normalize(a))[0]))
print("Уникальных слов:",len(set(tokenize(normalize(a))[0])))
print("Топ-5: ")
print("слово"+" "*(k-len("слово"))+"| частота")
print("-"*k*2)
for i in range(len(set(tokenize(normalize(a))[0]))):
    print(top_n(count_freq(tokenize(normalize(a))[0]))[i][1]+" "*(k-len(top_n(count_freq(tokenize(normalize(a))[0]))[i][1]))+"| "+\
          str(top_n(count_freq(tokenize(normalize(a))[0]))[i][0]))
#запуск     py .\src\lab03\text_stats.py

from src.lib.text import normalize,tokenize,count_freq,top_n
import math
def top_n_table(a,n):
    k=0
    for i in range(len(tokenize(normalize(a)))):
        if len(tokenize(normalize(a))[i])>k:
            k=len(tokenize(normalize(a))[i])
    k=k+5
    print(a)
    print("Всего слов:",len(tokenize(normalize(a))))
    print("Уникальных слов:",len(set(tokenize(normalize(a)))))
    print("Топ-5: ")
    print("слово"+" "*n*(k-len("слово"))+"|"*n+" частота")
    if k>0 and n>0:
        print("-"*k*2*n)
    a1=top_n(count_freq(tokenize(normalize(a))),5)
    if len(a1)<5:
        for i in range(len(a1)):
            print(a1[i][0]+" "*n*(k-len(a1[i][0]))+"|"*n+" "+str(a1[i][1]))
    else:
        for i in range(5):
            print(a1[i][0]+" "*n*(k-len(a1[i][0]))+"|"*n+" "+str(a1[i][1]))

'''
a=["ПрИвЕт\nМИр\t","ёжик, Ёлка","Hello\r\nWorld","  двойные   пробелы  "]
b=["привет мир","hello,world!!!","по-настоящему круто","2025 год","emoji 😀 не слово"]
c=["ad","ac","ab","aa","ba"]
d=["bb","aa","bb","aa","cc"]
n=4

print("normalize")
for x in range(len(a)):
    print(a[x]," → ",normalize(a[x]))
print(" ")
print("tokenize")
for x in range(len(b)):
    print(b[x]," → ",tokenize(b[x]))
print(" ")
print("count_freq + top_n")
print(c," → ",count_freq(c))
print(count_freq(c)," → ",top_n(count_freq(c),n))
print(" ")
print(d," → ",count_freq(d))
print(count_freq(d)," → ",top_n(count_freq(d),n))
'''
#python -m src.lab03.test_case_text
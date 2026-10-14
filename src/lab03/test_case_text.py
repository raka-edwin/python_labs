from src.lib.text import normalize,tokenize,count_freq,top_n

a=["ПрИвЕт\nМИр\t","ёжик, Ёлка","Hello\r\nWorld","  двойные   пробелы  "]
b=["привет мир","hello,world!!!","по-настоящему круто","2025 год","emoji 😀 не слово"]
c=["a","b","a","c","b","a"]
d=["bb","aa","bb","aa","cc"]
n=2

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
#python -m src.lab03.test_case_text
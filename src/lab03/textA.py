import re
def flatten(a):
    b=[]
    u=0
    for x in range(len(a)):
        if isinstance(a[x], (list, tuple)):
            u+=1
            for y in range(len(a[x])):
                b.append(a[x][y])
    if u==len(a):
        return b
    else:
        return TypeError
    
def normalize(a):
    b=[]
    for i in range(len(a)):
        b.append(a[i].replace("\n"," ").replace("\t"," ").replace("\r"," ").casefold().replace("ё","е").strip())
        k=b[i].count(" ")
        prob=" "*k
        b[i]=b[i].replace(prob," ")
    return b

def tokenize(a):
    b=[]
    for i in range(len(a)):
        b.append(re.split(r'[^a-zA-Z0-9а-яА-Я-]+',a[i]))
    for x in range(len(b)):
        for y in range(len(b[x])):
            if len(b[x][y])==0:
                b[x].pop(y)
    return b

def count_freq(a):
    b=set(a)
    freq=[[] for t in range(len(b))]
    for i in range(len(b)):
        freq[i].append(list(b)[i])
        freq[i].append(a.count(list(b)[i]))
    freq.sort()
    return freq

def alf_ord(a):
    num_of_nums=[]
    for i in range(len(a)):
        num_of_nums.append(a[i][0])
    num_of_nums=list(set(num_of_nums))
    num_of_nums.reverse()
    b=[[]for x in range(len(num_of_nums))]
    for x in range(0,len(num_of_nums)):
        for y in range(0,len(a)):
            if int(a[y][0])==int(num_of_nums[x]):
                b[x].append(a[y])
    for i in range(len(b)):
        b[i].sort()
    return flatten(b)

def top_n(a):
    b=[[0,0]for i in range(len(a))]
    for i in range(len(a)):
        b[i][0],b[i][1]=a[i][1],a[i][0]
    b.sort(reverse=True)
    return alf_ord(b)

a=["ПрИвЕт\nМИр\t","ёжик, Ёлка","Hello\r\nWorld","  двойные         пробелы  "]
b=["привет мир","hello,world!!!","по-настоящему круто","2025 год","emoji 😀 не слово"]
c=["a","b","a","c","b","a"]
print(a," → ",normalize(a))
print(b," → ",tokenize(b))
n=2
print(c," → ",top_n(count_freq(c))[0:n])
#запуск     py .\src\lab03\textA.py
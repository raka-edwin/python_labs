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
    b=""
    b=(a.replace("\n"," ").replace("\t"," ").replace("\r"," ").casefold().replace("ё","е").strip())
    c=""
    for i in range(len(b)-1):
        if b[i]==" " and b[i+1]==" ":
            pass
        else:
            c+=b[i]
    return c+b[-1]

def tokenize(a):
    b=[]
    c=[]
    b=(re.split(r'[^a-zA-Z0-9а-яА-Я-_]+',a))
    for x in range(len(b)):
        if len(b[x])==0:
            pass
        else:
            c.append(b[x])
    return c

def count_freq(a):
    b=set(a)
    freq=[[] for t in range(len(b))]
    for i in range(len(b)):
        freq[i].append(list(b)[i])
        freq[i].append(a.count(list(b)[i]))
    freq.sort()
    return dict(freq)

def alf_ord(a):
    num_of_nums=[]
    for i in range(len(a)):
        num_of_nums.append(a[i][1])
    num_of_nums=list(set(num_of_nums))
    num_of_nums.reverse()
    b=[[]for x in range(len(num_of_nums))]
    for x in range(0,len(num_of_nums)):
        for y in range(0,len(a)):
            if (a[y][1])==(num_of_nums[x]):
                b[x].append(a[y])
    for i in range(len(b)):
        b[i].sort()
        flatten(b[i])
    return flatten(b)

def top_n(a,n):
    c=list(dict.items(a))
    e=sorted(c, key=lambda x: x[1], reverse=True)
    return alf_ord(e[0:n])


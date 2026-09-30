import re
def min_max(a):
    for t in range(len(a)):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a[0],a[-1]

def unique_sorted(b):
    b=list(set(b))
    for t in range(len(b)):
            for i in range(len(b)-1):
                if b[i]>b[i+1]:
                    b[i],b[i+1]=b[i+1],b[i]
    return b

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

def transpose(mat):
    if len(mat)==0:
        return []
    else:
        m=len(mat)
        n=len(mat[0])
        mat2=[[0 for i in range(m)]for i in range(n)]
        for x in range(0,m):
            for y in range(0,n):
                mat2[y][x]=mat[x][y]
        return mat2

def row_sums(mat):
    m=len(mat)
    matrix_row_sum=[[]for i in range(m)]
    for i in range(0,m):
        matrix_row_sum[i].append(sum(mat[i]))
    return matrix_row_sum

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
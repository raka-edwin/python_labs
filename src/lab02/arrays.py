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
    
a=[[3,-1,5,5,0],[42],[-5,-2,-9],[],[1.5,2,2.0,-3.1]]
b=[[3,1,2,1,3],[],[-1,-1,0,2,2],[1.0,1,2.5,2.5,0]]
c=[[[1,2],[3,4]],[[1,2],(3,4,5)],[[1],[], [2,3]],[[1,2],"ab"]]

print("min_max")
for i in range(0,len(a)):
    if len(a[i])>0:
        print(a[i]," → ",min_max(a[i]))
    else:
        print(a[i]," → ",ValueError)
print(" ")
print("unique_sorted")
for i in range(0,len(b)):
    print(b[i]," → ",unique_sorted(b[i]))
print(" ")
print("flatten")
for i in range(0,len(c)):
    print(c[i]," → ",flatten(c[i]))
#запуск      py .\src\lab02\arrays.py
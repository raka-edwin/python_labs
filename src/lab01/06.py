n=int(input("in_1 "))
list1=[]
och=0
zaoch=0
for i in range(n):
    k=input("in_"+str(i+2)+" " )
    list1.append(k.split())
for i in range(n):
    if list1[i][3].count("True")==1:
        och+=1
zaoch=n-och
print("Out:",och,zaoch)
#запуск     py .\src\lab01\06.py
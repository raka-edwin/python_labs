a=input("a: ")
b=input("b: ")
if str(a).count(",")==1:
    a=float(str(a).replace(",","."))
else:
    a=float(str(a))
if str(b).count(",")==1:
    b=float(str(b).replace(",","."))
else:
    b=float(str(b))
print("sum="+str(int((100*(a+b)))/100)+";","avg="+str(int((a+b)*50)/100))
#запуск     py .\src\lab01\02_sum_avg.py
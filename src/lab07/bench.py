import csv
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort,selection_sort,insertion_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lib.text import flatten
from pathlib import Path
import random

def read_numbers(path):
    a=[]
    with open(path, encoding="utf-8") as f:
        r=csv.reader(f)
        for i in r:
            a.append(i)
        return a
 
 
def bench_sorts(n):
    datastr = flatten(read_numbers(f"data/lab07/samples/numbers_{n}.csv"))
    data=[int(x) for x in datastr]
    rows = []
    t1 = timeit.timeit(lambda: sorted(data), number=1)
    t2 = timeit.timeit(lambda: bubble_sort(data), number=1)
    t3 = timeit.timeit(lambda: selection_sort(data), number=1)
    t4 = timeit.timeit(lambda: insertion_sort(data), number=1)
    if int(t1)>60:
        rows.append(["sort", n, "sorted", ">60", "с"])
    elif t1<0.001:
        rows.append(["sort", n, "sorted", f"{t1*1000:.3f}", "мс"])
    else:
        rows.append(["sort", n, "sorted", f"{t1:.3f}", "с"])
    if int(t2)>60:
        rows.append(["sort", n, "bubble_sort", ">60", "с"])
    elif t2<0.001:
        rows.append(["sort", n, "bubble_sort", f"{t2*1000:.3f}", "мс"])
    else:
        rows.append(["sort", n, "bubble_sort", f"{t2:.3f}", "с"])
    if int(t3)>60:
        rows.append(["sort", n, "selection_sort", ">60", "с"])
    elif t3<0.001:
        rows.append(["sort", n, "selection_sort", f"{t3*1000:.3f}", "мс"])
    else:
        rows.append(["sort", n, "selection_sort", f"{t3:.3f}", "с"])
    if int(t4)>60:
        rows.append(["sort", n, "insertion_sort", ">60", "с"])
    elif t4<0.001:
        rows.append(["sort", n, "insertion_sort", f"{t4*1000:.3f}", "мс"])
    else:
        rows.append(["sort", n, "insertion_sort", f"{t4:.3f}", "с"])
    return rows

def bench_search(n):
    datastr = flatten(read_numbers(f"data/lab07/samples/numbers_{n}.csv"))
    target=random.randint(-100,100)
    data=[int(x) for x in datastr]
    rows = []
    if target in data:
        t1 = timeit.timeit(lambda: data.index(target), number=1)
    else:
        t1 = timeit.timeit(lambda: data.index(data[-1]), number=1)
    t2 = timeit.timeit(lambda: linear_search(data,target), number=1)
    t3 = timeit.timeit(lambda: binary_search(data,target), number=1)
    t3sort=timeit.timeit(lambda: sorted(data), number=1)
    sdata=sorted(data)
    if int(t1)>60:
        rows.append(["search", n, "list.index", ">60", "с"])
    elif t1<0.001:
        rows.append(["search", n, "list.index", f"{t1*1000:.3f}", "мс"])
    else:
        rows.append(["search", n, "list.index", f"{t1:.3f}", "с"])
    if int(t2)>60:
        rows.append(["search", n, "linear_search", ">60", "с"])
    elif t2<0.001:
        rows.append(["search", n, "linear_search", f"{t2*1000:.3f}", "мс"])
    else:
        rows.append(["search", n, "linear_search", f"{t2:.3f}", "с"])
    if int(t3)>60:
        rows.append(["search", n, "binary_search", ">60", "с", "сортировка", f"{t3sort:.3f}", "с"])
    elif t3<0.001:
        rows.append(["search", n, "binary_search", f"{t3*1000:.3f}", "мс", "сортировка", f"{t3sort:.3f}", "с"])
    else:
        rows.append(["search", n, "binary_search", f"{t3:.3f}", "с", "сортировка", f"{t3sort:.3f}", "с"])
    return rows

def bench_two_sum(n):
    datastr = flatten(read_numbers(f"data/lab07/samples/numbers_{n}.csv"))
    data=[int(x) for x in datastr]
    rows = []
    t1 = timeit.timeit(lambda: two_sum_brute(data,random.choice(data)), number=100)
    t2 = timeit.timeit(lambda: two_sum_fast(data,random.choice(data)), number=100)
    if int(t1/100)>60:
        rows.append(["two_sum", n, "two_sum_brute", ">60", "с"])
    elif t1/100<0.001:
        rows.append(["two_sum", n, "two_sum_brute", f"{t1*10:.3f}", "мс"])
    else:
        rows.append(["two_sum", n, "two_sum_brute", f"{t1/100:.3f}", "с"])
    if int(t2/100)>60:
        rows.append(["two_sum", n, "two_sum_fast", ">60", "с"])
    elif t2/100<0.001:
        rows.append(["two_sum", n, "two_sum_fast", f"{t2*10:.3f}", "мс"])
    else:
        rows.append(["two_sum", n, "two_sum_fast", f"{t2/100:.3f}", "с"])
    return rows

def count_x(t1,c1,t2,c2):
    t1=float(t1)
    t2=float(t2)
    if (c1=="с" and c2=="с") or (c1=="мс" and c2=="мс"):
        return f"{t2/t1:.1f}x"
    if c1=="мс" and c2=="с":
        return f"{t2/(t1/1000):.1f}x"

n3sort=(bench_sorts(1000))
n4sort=(bench_sorts(10000))
#n5sort=(bench_sorts(100000))
n4sort[0].insert(5,count_x(n3sort[0][3],n3sort[0][4],n4sort[0][3],n4sort[0][4]))
n4sort[1].insert(5,count_x(n3sort[1][3],n3sort[1][4],n4sort[1][3],n4sort[1][4]))
n4sort[2].insert(5,count_x(n3sort[2][3],n3sort[2][4],n4sort[2][3],n4sort[2][4]))
n4sort[3].insert(5,count_x(n3sort[3][3],n3sort[3][4],n4sort[3][3],n4sort[3][4]))
'''
if n5sort[0][3]!=">60" and n5sort[0][4]!=">60":
    n5sort[0].insert(5,count_x(n4sort[0][3],n4sort[0][4],n5sort[0][3],n5sort[0][4]))
if n5sort[1][3]!=">60" and n5sort[1][4]!=">60":
    n5sort[1].insert(5,count_x(n4sort[1][3],n4sort[1][4],n5sort[1][3],n5sort[1][4]))
if n5sort[2][3]!=">60" and n5sort[2][4]!=">60":
    n5sort[2].insert(5,count_x(n4sort[2][3],n4sort[2][4],n5sort[2][3],n5sort[2][4]))
if n5sort[3][3]!=">60" and n5sort[3][4]!=">60":
    n5sort[3].insert(5,count_x(n4sort[3][3],n4sort[3][4],n5sort[3][3],n5sort[3][4]))
'''
csv_list1=[["sorted"],n3sort[0],n4sort[0],\
          ["bubble_sort"],n3sort[1],n4sort[1],\
          ["selection_sort"],n3sort[2],n4sort[2],\
          ["insertion_sort"],n3sort[3],n4sort[3]]
write_csv(csv_list1,"data/lab07/out/bench_sort.csv")

n3search=(bench_search(1000))
n4search=(bench_search(10000))
n5search=(bench_search(100000))

csv_list2=[["list.index"],n3search[0],n4search[0],n5search[0],\
          ["linear_search"],n3search[1],n4search[1],n5search[1],\
          ["binary_search"],n3search[2],n4search[2],n5search[2]]
write_csv(csv_list2,"data/lab07/out/bench_search.csv")

n3two_sum=(bench_two_sum(1000))
n4two_sum=(bench_two_sum(10000))
n5two_sum=(bench_two_sum(100000))

csv_list3=[["two_sum_brute"],n3two_sum[0],n4two_sum[0],n5two_sum[0],\
          ["two_sum_fast"],n3two_sum[1],n4two_sum[1],n5two_sum[1]]
write_csv(csv_list3,"data/lab07/out/bench_two_sum.csv")

space=""
with open("data/lab07/out/bench_sort.csv","r", encoding="utf-8") as f:
    r=csv.reader(f)
    for t in r:
        for i in range(len(t)):
            if i in [0,1]:
                space=space+(t[i])+" "*(8-len(t[i]))
            if i==5:
                space=space+" "*(7-len(t[i]))+(t[i])
            if i==3:
                space=space+(t[i])
            if i==4:
                space=space+(t[i])+" "*(3-len(t[i]))
            if i==2:
                space=space+(t[i])+" "*(17-len(t[i]))
        print(space)
        space=""
print(" ")
space=""
with open("data/lab07/out/bench_search.csv","r", encoding="utf-8") as f:
    r=csv.reader(f)
    for t in r:
        for i in range(len(t)):
            if i in [0,1]:
                space=space+(t[i])+" "*(8-len(t[i]))
            if i==5:
                space=space+(t[i])+" "*(12-len(t[i]))
            if i==3 or i==6 or i==7:
                space=space+(t[i])
            if i==4:
                space=space+(t[i])+" "*(3-len(t[i]))
            if i==2:
                space=space+(t[i])+" "*(15-len(t[i]))
        print(space)
        space=""
print(" ")

space=""
with open("data/lab07/out/bench_two_sum.csv","r", encoding="utf-8") as f:
    r=csv.reader(f)
    for t in r:
        for i in range(len(t)):
            if i in [0,1]:
                space=space+(t[i])+" "*(8-len(t[i]))
            if i==5:
                space=space+(t[i])+" "*(12-len(t[i]))
            if i==3 or i==6 or i==7:
                space=space+(t[i])
            if i==4:
                space=space+(t[i])+" "*(3-len(t[i]))
            if i==2:
                space=space+(t[i])+" "*(15-len(t[i]))
        print(space)
        space=""
#     python -m src.lab07.bench
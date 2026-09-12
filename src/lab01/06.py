n=5
list1=[]
in_1="Максимов Максим 18 True"
list1.append(in_1)
in_2="Геннадьев Геннадий 17 False"
list1.append(in_2)
in_3="Алексеев Алексей 17 True"
list1.append(in_3)
in_4="Дмитриев Дмитрий 18 False"
list1.append(in_4)
in_5="Андреев Андрей 18 True"
list1.append(in_5)
очно=0
заочно=0
for i in range(0,n):
    if list1[i].count("T")==1:
        очно+=1
    else:
        заочно+=1
print(очно,заочно)
info=[("Иванов Иван Иванович", "BIVT-25", 4.6),("Петров Пётр", "IKBO-12", 5.0),\
      ("Петров Пётр Петрович", "IKBO-12", 5.0),("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]
name=[]
group=[]
gpa=[]
for a in range(0,len(info)):
    if len(info[a][0].split())==3:
        name.append(((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
    ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][1:]+" "+\
    ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[1][0].upper()+"."+\
    ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[2][0].upper()+".")
    if len(info[a][0].split())==2:
        name.append(((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
        ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][1:]+" "+\
        ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[1][0].upper()+".")
    if len(info[a][0].split())==1:
            name.append(((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
        ((str(info[a]))[1:-2].split(","))[0][1:-1].split()[0][1:])
    if len(info[a][0].split())==0:
        name.append("")

for a in range(0,len(info)):
    group.append(((str(info[a]))[1:-2].split(","))[1][2:-1])

for a in range(0,len(info)):
    gpa.append(round(float((str(info[a]))[2:-1].split(",")[2]),2))

for a in range(0,len(info)):

    if len(name[a])==0 or len(group[a])==0 or name[a][0]\
          not in ("ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"):
        print(str(info[a])," → ",TypeError)

    if gpa[a]<0 or gpa[a]>5 or len(name[a].split())<2 or len(name[a].split())>3:
        print(str(info[a])," → ",ValueError)

    if len(name[a])!=0 and len(group[a])!=0 and 0<=gpa[a]<=5 and\
         len(name[a].split())>=2 and name[a][0] in ("ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"):
        print(str(info[a])," → ",str(name[a])+", "+"гр. "+str(group[a])+", "+"GPA "+str(gpa[a]))
#запуск      py .\src\lab02\tuples.py
def format_record(text):
    name=""
    group=""
    gpa=0
    info=list(text)
    if len(info[0].split())==3:
            name=(((str(info))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
    ((str(info))[1:-2].split(","))[0][1:-1].split()[0][1:]+" "+\
    ((str(info))[1:-2].split(","))[0][1:-1].split()[1][0].upper()+"."+\
    ((str(info))[1:-2].split(","))[0][1:-1].split()[2][0].upper()+".")
    if len(info[0].split())==2:
            name=(((str(info))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
        ((str(info))[1:-2].split(","))[0][1:-1].split()[0][1:]+" "+\
        ((str(info))[1:-2].split(","))[0][1:-1].split()[1][0].upper()+".")
    if len(info[0].split())==1:
            name=(((str(info))[1:-2].split(","))[0][1:-1].split()[0][0].upper()+\
        ((str(info))[1:-2].split(","))[0][1:-1].split()[0][1:])
    if len(info[0].split())==0:
            name.join("")

    group=(((str(info))[1:-2].split(","))[1][2:-1])

    gpa=float(str(round(float((str(info))[2:-1].split(",")[2]),2)))

    if len(name)!=0 and len(group)!=0 and 0<=gpa<=5 and\
            len(name.split())>=2 and name[0] in ("ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"):
            return ((str(name)+", "+"гр. "+str(group)+", "+"GPA "+str(gpa)))
    
    if len(name)==0 or len(group)==0 or name[0] not in ("ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM"):
        return TypeError

    if gpa<0 or gpa>5 or len(name.split())<2 or len(name.split())>3:
        return ValueError

    
info=[("Иванов Иван Иванович", "BIVT-25", 4.6),("Петров Пётр", "IKBO-12", 5.0),\
      ("Петров Пётр Петрович", "IKBO-12", 5.0),("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]
info_test=[("Петоров", "BIVT-25", 3.5),("Петоров Пётр", "BIVT-25", 6.7),("Петоров Пётр", "", 4.7)]

for x in range(len(info)):
    print(info[x]," → ",format_record(info[x]))
    

print(" ")
print("доп тест-кейсы:")

for x in range(len(info_test)):
    print(info_test[x]," → ",format_record(info_test[x]))
#запуск      py .\src\lab02\tuples.py
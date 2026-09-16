fio=input("ФИО: ")
initials=""
for i in range(len(fio)-1):
    if fio[i] in "ЁЙЦУКЕНГШЩЗХЪЖЭДЛОРПАВЫФЯЧСМИТЬБЮ":
        initials+=fio[i]
print("Инициалы:",initials + ".")
print("Длина (символов):",len(fio)-fio.count(" ")+2)
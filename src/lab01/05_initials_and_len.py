fio=input("ФИО: ")
initials=""
a=fio.split()
print("Инициалы:",a[0][0].upper()+a[1][0].upper()+a[2][0].upper()+ ".")
print("Длина (символов):",len(fio)-fio.count(" ")+2)
#запуск     py .\src\lab01\05_initials_and_len.py
m=int(input("Минуты: "))
if m-(m//60*60)>=10:
    print(str(m//60) + ":" + str(m-int(m/60)*60))
else:
    print(str(m//60) + ":0" + str(m-int(m/60)*60))
#запуск     py .\src\lab01\04_minutes_to_hhmm.py
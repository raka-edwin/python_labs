fio=" Борбатенко Никита Янович"
initials=""
for i in range(len(fio)-1):
    if fio[i]==" ":
        initials+=fio[i+1]
print(initials + ".")
print(len(fio)-1)
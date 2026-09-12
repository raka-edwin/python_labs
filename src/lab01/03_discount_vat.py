price=1250.5
discount=10
vat=20
print("База после скидки:", str(round((price*(1-(discount/100))),2))+"₽")
print("НДС:",  str(round(((vat/100)*price*(1-(discount/100))),2))+"₽")
print("Итого к оплате:",  str(round(round((price*(1-(discount/100))),2)+ round(((vat/100)*price*(1-(discount/100))),2),2))+"₽")
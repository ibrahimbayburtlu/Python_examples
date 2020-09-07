boy=int(input("Boyunuz (cm olarak):"))
kilo=float(input("Kilonuz (kg olarak):"))
bki=kilo/((boy*boy)/10000)

if bki<18:
    print("Beden kitke indeksiniz {},Zayıfsınız!".format(bki))
elif bki<25:
    print("Beden kitle indeksiniz {},İdeal BKI'ye sahipsiniz!".format(bki))
elif bki<30:
    print("beden Kitle indeksiniz {},kilolusunuz!".format(bki))
elif bki<35:
    print("Beden kitle indeksiniz {},1.Dereceden Obezsiniz!".format(bki))
elif bki <40:
    print("Beden kitle indeksiniz{},2.dereceden Obezsiniz!".format(bki))
else:
    print("Beden kitle indeksiniz {}, 3. dereceden Morbid Obezsiniz".format(bki))

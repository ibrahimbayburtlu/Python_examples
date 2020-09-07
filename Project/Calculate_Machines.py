sayı_1=int(input("1.sayiyi girin:"))
sayı_2=int(input("2.sayiyi girin:"))

seçim=int(input("Seçimi yapın:\n1. Toplama\n2. Cıkarma\n3.Çarpma\n4.Bölme"))

if seçim==1:
    print("Sonuç{}".format(sayı_1+sayı_2))
elif seçim==2:
    print("Sonuç{}".format(sayı_1-sayı_2))
elif seçim==3:
    print("Sonuç{}".format(sayı_1*sayı_2))
elif seçim==4:
    print("Sonuç{}".format(sayı_1/sayı_2))
else:
    print("Hatalı giriş yaptınız.")
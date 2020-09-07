# def fonksiyon_Adi(parametre1,parametre2):
    
#             işlemler

# fonksiyon_Adi()



# def person():
#     print("Selam naber")
# person()


# def toplama(sayı_1,sayı_2):
#     return sayı_1+sayı_2
# print(toplama(5,7 ))

# def toplama(sayı_1=12,sayı_2=13):
#     return sayı_1+sayı_2
# print("Sonuç:",toplama())

# def toplama(sayı_1=12,sayı_2=13):
#     print(sayı_1+sayı_2)
# toplama(15,17)

# def toplama(sayı_1,sayı_2):
#     return sayı_1+sayı_2

# sayı_1=int(input("Lütfen bir sayı giriniz:"))
# sayı_2=int(input("Lütfen bir sayı giriniz:"))

# print("Sonuç:",toplama(sayı_1,sayı_2))

# def toplama(sayı_1,sayı_2):
#     return sayı_1+sayı_2
# def cıkarma(sayı_1+sayı_2):
#     return sayı_1-sayı_2
# def carpma(sayı_1,sayı_2):
#     return sayı_1*sayı_2
# def bolme(sayı_1,sayı_2):
#     return sayı_1/sayı_2

# while True:
#     secim=input("Lütfen bir seçim yapınız:")
#     if secim=="q":
#         exit()
# sayi1 = int(input("Birinci sayıyı girin :"))
# sayi2 = int(input("İkinci sayıyı girin :"))
# if secim=="1":
#     print("Sonuç :", toplama(sayi1, sayi2))
# elif secim =="2":
#     print("Sonuç :", cikarma(sayi1,sayi2))
# elif secim =="3":
#     print("Sonuc :",carpma(sayi1,sayi2))
# elif secim=="4":
#     print("Sonuç :",bolme(sayi1,sayi2))
# else:
#     print("Yanlış seçim lütfen tekrar deneyin")
#     exit()


# def ortHesapla(liste):
#     ort=sum(liste)/len(liste)
#     return ort
# def standartHesapla(liste):
#     standartKarekok=[]
#     for i in range(len(liste)):
#         standartKarekok.append((liste[i]-ortHesapla(liste))**2)
#         standartSapma=(sum(standartKarekok)/len(liste)-1)**0.5
#         return standartSapma
# liste=[23,45,67,89,12,5]
# print("Satndart Sapma:",standartHesapla(liste))


# def fibonacci(sayi):
#     if sayi==0:
#         return 0
#     if sayi==1:
#         return 1
#     return fibonacci(sayi-1)+(sayi-2)
# sayi=int(input("Bir sayı gir:"))
# print(fibonacci(sayi))

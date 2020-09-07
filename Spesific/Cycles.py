# #While Döngüsü

# a=1
# b=10
# while a<b:
#     print(a,end=" ")
#     a+=1 #a=a+1 ile aynı

# ördüğünüz gibi while komutunun yapısı if‘e benziyor:
#  İkisi de bir şarttan sonra iki nokta üstüste (:) ile bir blok başlatıyor, ve blok içeri doğru kaydırılıyor.

# a=1
# b=10
# toplam=0
# while a<=10:
#     toplam+=a
#     a+=1
# print(toplam)

# a=1
# b=101
# toplam=0
# while a<=b:
#     toplam+=a
#     a+=2
# print(toplam)

# a=1/2
# b=1/1024
# toplam=0
# while b<=a:
#     toplam+=b
#     b*=2
# print(toplam)


# a=1
# b=100
# toplam=0
# while a<=100:
#     toplam+=a*2
#     a+=1
# print(toplam)

# p=1
# a=1
# a=10
# toplam=0
# while a<=10:
#     toplam +=a**p
#     a+=1
# print("p="p,p",)


# break: Döngüyü bitirmek
# Bir döngü bloku içinde verilen bir break komutu, döngünün hemen o anda bitirilmesine yol açar.
# Program akışı döngü blokunun dışına atlar, ve ardından gelen komutlarla devam eder. 

# toplam=0
# while True:  #Şart hep doğru-sonsuz döngü
#     x=int(input("Bir Sayı girin:(bitirmek için -99)"))
#     if x==-99:
#         break
#     toplam+=x
#     print("toplam:",toplam)

# break sadece döngüler içinde ve bir if şartı altında bir mânâ ifade eder.
# Eğer if kullanmazsanız Python yorumlayıcısı döngünün ilk iterasyonunda break‘e rastlayarak döngüyü tamamlar, blokun geri kalanını hiç işlemez.

# continue: Döngünün kalanını atlamak

# continue komutu da, aynı break gibi, sadece bir döngü içinde ve bir if şartı altında mânâ ifade eder.
# continue döngü blokunun işlemesini yarıda keser ve başa döner. break‘den farkı, programın döngünün dışına çıkmaması, ama döngünün başına dönmesi ve tekrar başlatmasıdır. 

# toplam=0
# while True:
#     x=int(input("Lütfen Bir sayı girin:(bitirmek için -99"))
#     if x==-99:
#         break
#     if x<0 or x>100:
#         print("0-100 arası olamlı")
#         continue
#     toplam+=x
# print("Toplam:",toplam)

# else
# Python dilinde while ve for döngülerinde bir else bloku bulunabilmesi mümkündü.

# data = [1,2,4,-1,3,4,-5,1]
# i = 0
# aranan = 3

# bulduk = False
# while i<len(data) and not bulduk:
#     if data[i] == aranan:
#         bulduk = True
#     else:
#         i += 1

# if bulduk:
#     print("Aranan", aranan, "değeri", i, "pozisyonunda.")
# else:
#     print("Bulamadık")

# data = [1,2,4,-1,3,4,-5,1]
# i = 0
# aranan = int(input("Aranan değer: "))

# while i<len(data):
#     if data[i] == aranan:
#         print ("Aranan", aranan, "değeri", i, "pozisyonunda.")
#         break;
#     i += 1
# else:
#     print("Bulamadık")

# x=int(input("Bir Pozitif tamsayı girin:"))
# asal=True
# i=2
# while i*i<=x and asal:
#     if x%i==0:
#         asal=False
#     else:
#         i+=1

# if asal:
#     print("Asal.")
# else:
#     print("Asal değil,", i, "böler.")

# x = int(input("Bir pozitif tamsayı girin: "))
# i = 2
# while i*i <= x:
#     if x % i == 0:
#         print("Asal değil,", i, "böler.")
#         break
#     i += 1
# else:
#     print("Asal.")
    
# for: Sıralı nesneler üzerinde döngü
# python’da for başka bir görev üstlenmiştir: Liste, dize, çokuz gibi sıralı bir nesnedeki elemanları sırayla tek tek alır ve döngü blokunda işler.    


# for s in ["fındık","fıstık","ceviz"]:
#     print(s)

# L=["fındık","fıstık","ceviz"]
# i=0
# while i<len(L):
#     print(L[i])
#     i+=1

# for x in range(11):
#     print(x, x**2)

# for c in "merhaba":
#     print(c,end=",")

# toplam=0
# for x in (4,5,2,-4,1,10):
#     toplam+=x
# print(toplam)

# toplam=0
# L=(4,5,2,-4,1,10)
# for x in L:
#     toplam=toplam+x
# print(toplam)

L = [(1,2), (2,4), (3,8)]
for e in L:  # her e'nin iki elemanı vardır
    print (e[0], e[1], e[0]+e[1])
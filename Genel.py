# #1: Ekrana “Merhaba Dünya” yazdıran Python örneği
# print("Merhaba Dünya!")

# #2: Yorum ve açıklama satırı örneği
# a=2

#Tek satırlı yorum ve açıklamalar “#” işareti ile yazılır.

# # Çok satırlı yorum ve açıklamalar ise 3 adet çift veya tek tırnakla başlar ve aynı işaretle sonlandırılır.
# # Yorum satırlarındaki kodlar işleme alınmaz.
# a = 10
# print(a)

# #3: Kullanıcının ismini alarak "Merhaba (kullanıcı ismi)" yazdıran Python örneği
# isim = input('İsminizi Girin : ')
# print("Merhaba " + isim)

# #4: Girilen 2 sayıyı toplayan Python örneği
# sayi1 = input('1. Sayı : ')
# sayi2 = input('2. Sayı : ')
# toplam = float(sayi1) + float(sayi2)
# print("Toplam :{0} ".format(toplam))

# #5: Girilen 2 sayının ortalamasını bulan Python örneği
# sayi1 = input('1. Sayı : ')
# sayi2 = input('2. Sayı : ')
# ortalama = (int(sayi1) + int(sayi2)) / 2
# print("Ortalama : {0} ".format(ortalama))

# #6: Girilen sayının asal sayı mı değil mi olduğunu bulan Python örneği
# sayac = 0
# sayi = input('Sayı: ')
# for i in range(2, int(sayi)):
#       if(int(sayi) % i == 0):
#             sayac += 1
#             break
# if(sayac != 0):
#       print("Sayı Asal Değil")
# else:
#       print("Sayı Asal")

# #7: Girilen vize ve final notu ortalaması hesaplayan Python örneği
# vize = input('Vize Notunuz : ')
# final = input('Final Notunuz : ')
# ortalama = (float(vize) * 0.3) + (float(final) * 0.7)
# print("Ortalama :{0} ".format(ortalama))

# #8: Girilen 3 yazılı notunun ortalamasını bulan Python örneği
# y1 = input('1. Yazılı : ')
# y2 = input('2. Yazılı : ')
# y3 = input('3. Yazılı : ')
# ortalama = (float(y1) + float(y2) + float(y3)) / 3
# print("Ortalama :{0} ".format(ortalama))

# #9: Yazılı ortalaması girilen öğrencinin sınıf geçme durumunu (GEÇTİ – KALDI) gösteren Python örneği
# ort = input('Ortalamanızı Girin : ')
# if(int(ort) >= 50):
#       print("Geçtiniz")
# else:
#       print("Kaldınız")

# #10: Girilen sayının tek mi Çift mi olduğunu bulan Python örneği.
# sayi = input('Sayı : ')
# if(int(sayi) % 2 == 0):
#       print("Sayı Çift")
# else:
#       print("Sayı Tek")

# #11: Girilen sayının pozitif, negatif, ya da sıfır olduğunu bulan Python örneği      
# sayi = input('Sayı : ')
# if(int(sayi) < 0):
#       print("Sayı Negatif")
# elif(int(sayi) > 0):
#       print("Sayı Pozitif")
# else:
#       print("Sayı Sıfır")

# #12: Yaşı girilen kişinin ehliyet alıp alamayacağını gösteren Python örneği
# yas = input('Yaşınız : ')
# if(int(yas) < 18):
#       print("Yaşınız Ehliyet almak için uygun değil")
# else:
#       print("Yaşınız Ehliyet almak için uygun")

# #13: 1-100 arası sayıları ekranda listeleyen Python örneği.
# for i in range(1, 101):
#         print(i)

# #14: 1-100 arası çift sayıları listeleyen Python örneği.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# #15: 1-100 arası tek sayıları listeleyen Python örneği
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i)

# #16: Kenarları girilen dikdörtgenin alanı ve çevresini bulan Python örneği
# kisa = input('Kısa Kenar : ')
# uzun = input('Uzun Kenar : ')
# alan = int(kisa) * int(uzun)
# cevre = 2 * (int(kisa) + int(uzun))
# print("Alan : {0}".format(alan))
# print("Çevre : {0}".format(cevre))
#         print(i)

# #17: Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python örneği.
# toplam = 0
# sayi1 = input('1. Sayı: ')
# sayi2 = input('2. Sayı: ')
# for i in range(int(sayi1) + 1, int(sayi2)):
#       toplam += i
# print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1, sayi2, toplam))

# #18: Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği:
# yeniMaas = 0
# maas = input("Maaşı Gir : ")
# zam = input("Zam Oranı(%) : ")
# yeniMaas = int(maas) + (int(maas) * int(zam) / 100)
# print("Zamlı Maaş :", yeniMaas)

# #19: Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan Python örneği:
# def daireAlan(yaricap):
#     alan = float(yaricap) * float(yaricap) * 3.14
#     print ("Alan :", alan)
#     return alan
# r = input("Yarıçapı Gir :")
# daireAlan(r)

# #20: Python ile sayı tahmin oyunu örneği:
# from random import randint
 
# rand = randint(1, 100)
# sayac = 0
 
# while True:
#     sayac += 1
#     sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
#     if(sayi == 0):
#         print("Oyunu İptal Ettiniz")
#         break
#     elif sayi < rand:
#         print("Daha Yüksek Bir Sayı Girin.")
#         continue
#     elif sayi > rand:
#         print("Daha Düşük Bir Sayı Girin.")
#         continue
#     else:
#         print("Rastele seçilen sayı {0}!".format(rand))
#         print("Tahmin sayınız {0}".format(sayac))



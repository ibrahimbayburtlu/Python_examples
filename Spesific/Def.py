# Python Fonksiyon Kullanımı

# def, fonksiyon tanımlamak için kullanılan bir anahtar kelimedir ve defined (tanımlamak) kelimesinin kısaltılmışından gelmektedir.
# Bizim fonksiyonları kullanmamızdaki temel  amacımız ise kod kalabalığını önlemek ve daha düzenli kod yazmaktır.

# def fonksiyon_adi():
#fonksiyon blogu,kodlar bu kısma yazılır...

# def deneme ():
#     print("Bir varmış,bir yokmuş")
# deneme() #Fonksiyon'un çagrılması

# def topla(sayı1,sayı2):#iki argüman alınacak
#     print(sayı1+sayı2)

# topla(13,8) # 13 ve 8 argüman olarak verildi,sayı1 ve sayı2'ye eşitlendi.

# def ort(s1,s2):
#     return (s1+s2)/2 #verilen iki sayının ortalamasını hesaplayıp,return ile dönüyoruz.
# sonuç=ort(6,2)
# print(sonuç,sonuç*4)

# Asallık testi

# def asal_mı(x):
#     i = 2
#     while i*i <= x:
#         if x % i == 0:
#             return False
#         i += 1
#     else:
#         return True

# Asal çarpanlar

# def asalçarpanlar(N):
#     çarpanlar = []  # boş liste    
#     x = 2
#     while N > 1:
#         # x asal mı?
#         asal = True
#         i = 2
#         while i*i <= x:
#             if x % i == 0:
#                 asal = False
#                 break
#             i += 1

#         if asal and N % x == 0:  # x asalsa ve N'yi bölüyorsa...
#             çarpanlar.append(x)  # x'i listenin sonuna ekle
#             while N % x == 0 :   # N x'e bölünebildiği sürece...
#                 N = N / x        # N'yi x'e böl, x çarpanı kalmasın.
#         x += 1
#     return çarpanlar

# saat=int(input("Lüften saati giriniz"))
# if saat<7 or saat>7: 
#     print("Uyumaya devam.") 
# elif saat==7: 
#     print("Alarm çalıyor, kalk!") 
# else: 
#     print("Lütfen bir saat giriniz.") 


meyve = input("Hangi meyveyi istiyorsun?")

if meyve ==("muz"):
     kilo = int(input("Kaç kilo muz istiyorsun?"))
     print(kilo*5,"tl ücret ödeyeceksiniz.")

elif meyve ==("elma"):
     renk = input("Hangi renk elma istiyorsun?")
     if renk == ("kırmızı"):
         kilo = int(input("Kaç kilo kırmızı elma istiyorsun?"))
     elif renk ==("sarı"):
         kilo = int(input("Kaç kilo sarı elma istiyorsun?"))
     elif renk ==("yeşil"):
         kilo = int(input("Kaç kilo yeşil elma istiyorsun?"))
     else:
         print("Sadece sarı, kırmızı ya da yeşil renk elma var.")

     print(kilo*2,"tl ücret ödeyeceksiniz.")

elif meyve == ("üzüm"):
     renk = input("Hangi renk üzüm istiyorsun?")
     if renk == ("mor"):
        kilo = int(input("Kaç kilo mor üzüm istiyorsun?"))
        print(kilo*3,"tl ücret ödeyeceksiniz.")
     elif renk ==("yeşil"):
        kilo = int(input("Kaç kilo yeşil üzüm istiyorsun?"))
        print(kilo*3.5,"tl ücret ödeyeceksiniz.")
     else:
       print("Sadece mor ya da yeşil renk üzüm var.")
        
else:
     print("Manavda sadece muz, elma ve üzüm var.")


     tekrar = int(input("Şimdi bir oyun oynayalım. Kaç kere oynamak istiyorsun? "))

for i in range (1,tekrar+1,1):
  print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daire seç.")
  print()
  tur = input("Hangi şekli istiyorsun ")

  if tur == "dik üçgen":
    satir = int(input("üçgen satır sayısını giriniz"))
    for sayi in range(1,satir+1,1):
      print(sayi*"*")

  elif tur == "eşkenar üçgen":
    satir = int(input("üçgen satır sayısını giriniz"))
    sayac = satir
    for sayi in range(1,satir+1):
      print(sayac*" ",(2*sayi-1)*"*")
      sayac-=1
      
  elif tur == "kare":
    satir = int(input("kare satır sayısını giriniz"))
    for dis in range(1,satir+1):
      for ic in range(1,satir+1):
          print("*", end=" ")
      print()

  elif tur =="dikdörtgen":
    satir = int(input("dikdörtgen satır sayısını giriniz"))
    sutun = int(input("dikdörtgen sütun sayısını giriniz"))
    for satir in range(1,satir+1):
      for sutun in range(1,sutun+1):
          print("*", end=" ")
      print()
      
  elif tur =="daire":
    satir = int(input("daire satır sayısını giriniz"))
    for sayi in range(satir):
      if sayi > satir/2:
        for k in range(satir-sayi):
          print(" ",end="")
        for m in range((sayi+2)*2-1):
          print("*",end="")
        print()

    for sayi in range(satir,0,-1):
      if sayi > satir/2:
        for k in range(satir-sayi):
          print(" ",end="")
        for m in range((sayi+2)*2-1):
          print("*",end="")
        print()
        
  else:
    print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daire seçebilirsiniz.")
    print()
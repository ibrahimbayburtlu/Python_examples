# Asal sayıları listelemek
# Bir önceki yazıda, belli bir sayının asal olup olmadığını tespit eden bir program yazmıştık.Bir önceki yazıda, belli bir sayının asal olup olmadığını tespit eden bir program yazmıştık.
# Burada, o programı 2 ile N arasındaki her tamsayı için çalıştıracağız.

# N=int(input("Bir pozitif tam sayı girin:"))
# x=2
# while x<=N:
#     i=2
#     while i*i<=x:
#         if x %i==0:
#             break
#         i+=1
#     else:
#         print(x)
#     x+=1

# Verilen bir sayının asal çarpanlarını listelemek

# N=int(input("Bir pozitif tamsayı girin:"))
# x=2
# while N>1:
#     # x asal mı?
#     asal=True
#     i=2
#     while i*i<=x:
#         if x%i==0:
#             asal=False
#             break
#         i+=1
    
#     if asal and N %x==0:
#         print(x,end=" ")
#         while N % x==0:
#             N=N/x
#     x+=1

# Fibonacci dizisi

# a,b=1,1
# print(a)
# print(b)
# i=2
# while i<50:
#     a,b=b,a+b
#     print(b)
#     i+=1

# a = 1
# b = 1
# print(a)
# print(b)
# i = 2
# while i<=50:
#     a_eski = a
#     b_eski = b
#     a = b_eski
#     b = a_eski + b_eski
#     print(b)
#     i += 1

# Collatz dizisi

# n=int(input("Başlangıc Degeri:"))
# while n>1:
#     if n%2==0: # n çift sayıysa
#         n=n/2
#     else: # n tek sayıysa
#         n=3*n+1
#     print(int(n),end=" ")

# # Seriler
# toplam = 0.0 # ara toplam
# isaret = 1 # +1 veya -1 olarak dönüşümlü olarak değişecek
# payda = 1.0  # 1,3,5,7,...
# terim = isaret / payda
# sayac = 1
# while abs(terim) > 0.00001:
#     toplam += terim
#     payda += 2
#     isaret *= -1
#     terim = isaret / payda
#     sayac += 1

# print("pi ~", 4*toplam)
# print(sayac,"terim toplandı.")


# # Fonksiyon tablolama

# import math 
# x=0.0
# dx=0.1
# print("x","sinx")
# while x <=1.0:
#     print(x,math.sin(x))
#     x+=dx

# import math
# x = 0.0
# dx = 0.1
# print("{:6s} {:6s}".format("x", "sin x"))
# while x <= 1.0:
#     print("{:1.4f} {:1.4f}".format(x, math.sin(x)))
#     x += dx

# # İteratif denklem sistemleri

# import math

# a,b,c = 1000, 0, 0
# N = a+b+c

# lam_a = math.log(2) / 6.57 # I-135, 1/saat biriminde
# lam_b = math.log(2) / 9.14 # Xe-135, 1/saat biriminde
# t = 0

# # Sütun başlıkları sağa yaslansın.
# print("{:>6s} {:>6s} {:>6s} {:>6s}".format("saat", "I","Xe","Cs"))

# # Bir saatlik aralıklarla a,b,c miktarını ekrana bas.
# while t <= 20:
#     print("{:6d} {:6d} {:6d} {:6d}".format(t, int(a), int(b), int(c)))
#     a = (1-lam_a)*a
#     b = (1-lam_b)*b + lam_a*a
#     c = N-a-b
#     t+=1
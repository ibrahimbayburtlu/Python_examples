# 2- Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur. Phytonda fibonacci dizisi nasıl yapılır kodlarını yazınız (ilk 10 sayı olsa yeterli)


# Sayı_1=int(input("Lütfen bir sayı giriniz:"))
def fibonacci(Sayı_1):
    if Sayı_1<2:
        print(Sayı_1)
    else:
        print(fibonacci(Sayı_1)+fibonacci(Sayı_1-1))
fibonacci(5)

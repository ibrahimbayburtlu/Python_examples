
#Value Error 
# try:
#     result=input("Lütfen Bir sayı giriniz:")
#     print("girdiginiz sayı {} teşekkür ederiz".format(result))
# except ValueError:
#     print("Lütfen bir sayı giriniz")




# ValueError ve ZeroDivisionError
# try:
#     sayı_1=int(input("Lütfen bir sayı giriniz(1.sayı):"))
#     sayı_2=int(input("Lütfen bir sayı giriniz(2.sayı):"))
#     print(float(sayı_1/sayı_2))
# except ZeroDivisionError:
#     print("Lütfen yeni bir sayı giriniz 2.sayı=0 degerine eşittir.")
#     sayı_2=int(input("Lütfen bir sayı giriniz(2.sayı):"))
#     print(float(sayı_1/sayı_2))
# except ValueError:
#     print("Lütfen girdiginiz degerlerin sayı olmasını dikkat edin...")
#     sayı_1=int(input("Lütfen bir sayı giriniz(1.sayı):"))
#     sayı_2=int(input("Lütfen bir sayı giriniz(2.sayı):"))
#     print(float(sayı_1/sayı_2))

i=3
if type(i) is int:
    raise TypeError("la bu sayıdır.")

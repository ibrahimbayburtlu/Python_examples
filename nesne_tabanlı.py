class Ogrenci:
    Ogrenci_sayisi=0
    def __init__(self,adi,numarasi):
        self.adi=adi
        self.numarasi=numarasi
        Ogrenci.Ogrenci_sayisi+=1

        def Ogrenci_sayisi(self):
            print("Toplam ögrenci:{}".format(Ogrenci.Ogrenci_sayisi))

        def OgrenciGoster(self):
            print(f"Adi:{self.adi},Numarasi:{self.numarasi}")

Ogr1=Ogrenci("ahmet",123)
Ogr2=Ogrenci("Mehmet",1234)
Ogr3=Ogrenci("Ayşe",12345)

Ogr1.Ogrenci_sayisi()
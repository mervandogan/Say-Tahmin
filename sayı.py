import random
import time

sayı=random.randint(0,100)
tahmin=5
while True:
    tahmin=int(input("Tahmininiz:"))

    if (tahmin<sayı):
        print("Daha yüksek bir sayı söyleyin...")
        tahmin-=1
    elif (tahmin>sayı):
        print("Daha düşük bir sayı giriniz... ")
        tahmin-=1
    else:
        print("Tebrikler Sayımız",sayı)
        break
    if (tahmin==0):
        print("Tahmin hakkınız bitmiştir.Sayı",sayı)
        break
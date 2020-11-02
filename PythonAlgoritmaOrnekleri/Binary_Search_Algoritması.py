"""
-----------------------------
@Author : Mehmetcan Dalmazgil
-----------------------------
@Kaynakça :
    --> Binary Search Algoritmasi : https://www.geeksforgeeks.org/python-program-for-binary-search/
    --> Random Sayi Uretimi : https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range
    --> Time Fonksiyonu Kullanimi : https://www.studytonight.com/post/calculate-time-taken-by-a-program-to-execute-in-python
    --> Sort Fonksiyonu Kullanimi : https://www.geeksforgeeks.org/sort-in-python/

    --> Binary Search Nedir? : https://medium.com/@tugrulbayrak/search-arama-algoritmalari-binary-linear-5260431ba9a3
    --> Big O Notasyonu Nedir? : https://medium.com/kodcular/nedir-bu-big-o-notation-b8b9f1416d30
    --> Global Degisken Nedir? : https://medium.com/kodelim/global-ve-yerel-de%C4%9Fi%C5%9Fkenler-9f4480db8402
"""

import random # Gerekli olan kutuphaneleri programimiza ekliyoruz.
import time

ilk_program = time.time() # Programimizin calisma suresini ogrenmek icin time kutuphanesini kullanarak kodun baslangic zamanini tutan bir degisken tanimliyoruz.

print("Binary Search Algoritmasi")
print("-------------------------\n")

def binary_arama(dizi, alt, ust, sayi):
    global ilk_binary # binary_arama fonksiyonumuzun calisma suresini hesaplamak icin degiskenler tanimliyoruz.
    global son_binary # Bu degiskenleri global olarak tanimlamamizin sebebi degiskenlere oldugu gibi fonksiyon disinda da erismektir.

    ilk_binary = time.time()
    if ust >= alt: # binary search algoritmasi mantigina gore if-else kosul ifadelerimizi duzenliyoruz.
        orta = (ust + alt) // 2
        if dizi[orta] == sayi:
            son_binary = time.time()
            return orta
        elif dizi[orta] > sayi:
            son_binary = time.time()
            return binary_arama(dizi, alt, ust - 1, sayi)
        else:
            son_binary = time.time()
            return binary_arama(dizi, orta + 1, ust, sayi)
    else:
        son_binary = time.time()
        return -1

dizi = []
for x in range (0,100): # Bu dongude 100 elemanlik, icindeki degerler 0-100 sayilari arasindan rastgele secilen bir dizi olusturuyoruz.
    dizi.append(random.randint(0,100)) # random() fonksiyonu yardimiyla olusturdugumuz her sayiyi dizimize append ediyoruz(ekliyoruz).
dizi.sort() # Binary Search algoritmasi mantigina gore dizi elemanlari kucukten buyuge dogru sirali olmasi gerektiginden dizideki elemanlarimizi sort() fonksiyonu yardimiyla siraliyoruz.

sayi = 16
sonuc = binary_arama(dizi, 0, len(dizi) - 1, sayi) # binary_arama algoritmamizin dondurdugu sonucu 'sonuc' adli degiskende sakliyoruz.

if sonuc != -1: # Algoritmanin dondurdugu degere gore if-else kosul ifadelerini olusturuyoruz.
    print(f"Aranan sayi dizinin {str(sonuc)}. indisinde bulunmaktadir.\n")
else:
    print("Aranan sayi dizide bulunmamaktadir.\n")

# Son olarak program ile binary_arama fonsiyonumuzun calisma surelerini hesaplayarak ekrana yazdiriyoruz.
zaman_binary = son_binary - ilk_binary
print(f"Calisma Suresi(Binary Arama) = {zaman_binary}\n")

son_program = time.time()
zaman_program = son_program - ilk_program
print(f"Calisma Suresi(Tum Program) = {zaman_program}\n")
# Not: Algoritmalarin ve programlarin calisma suresi BigO notasyonuyla(O(n)) tahmin edilebilmektedir.




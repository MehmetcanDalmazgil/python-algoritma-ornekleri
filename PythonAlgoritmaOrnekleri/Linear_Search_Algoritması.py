"""
-----------------------------
@Author : Mehmetcan Dalmazgil
-----------------------------
@Kaynakça :
    --> Linear Search Algoritmasi : https://www.tutorialspoint.com/linear-search-in-python-program
    --> Random Sayi Uretimi : https://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range
    --> Time Fonksiyonu Kullanimi : https://www.studytonight.com/post/calculate-time-taken-by-a-program-to-execute-in-python

    --> Linear Search Nedir? : https://medium.com/@tugrulbayrak/search-arama-algoritmalari-binary-linear-5260431ba9a3
    --> Big O Notasyonu Nedir? : https://medium.com/kodcular/nedir-bu-big-o-notation-b8b9f1416d30
    --> Global Degisken Nedir? : https://medium.com/kodelim/global-ve-yerel-de%C4%9Fi%C5%9Fkenler-9f4480db8402
"""

import random # Gerekli olan kutuphaneleri programimiza ekliyoruz.
import time

ilk_program = time.time() # Programimizin calisma suresini ogrenmek icin time kutuphanesini kullanarak kodun baslangic zamanini tutan bir degisken tanimliyoruz.

print("Linear Search Algoritmasi")
print("-------------------------\n")

def lineer_arama(dizi, sayi): # Bu fonksiyon ile list yapimizi dogrusal olarak tarayip icinde aradigimiz sayinin bulunup bulunadigini kontrol ediyoruz.
   global ilk_lineer # Fonksiyon icinde global olarak tanımlanan degiskenlere fonksiyon disindan erisebilmekteyiz.
   global son_lineer
   ilk_lineer = time.time() # Linear Search algoritmasinin calisma hizini ogrenmek icin time kutuphanesinden tekrar yararlaniyoruz.
   for i in range(len(dizi)): # for dongusu yardimiyla list yapimizda bulunan tum degerlerle sayimizi karsilastiriyoruz.
      if dizi[i] == sayi:
         son_lineer = time.time() # Algoritmanin calisma suresini bulmak icin algoritmanin sonlandigi andaki sureyi bir degiskene kaydediyoruz
         return i # Aramis oldugumuz sayi list icinde bulunuyorsa fonksiyon geriye aradigimiz sayiyi donduruyor.
   son_lineer = time.time()
   return -1 # Aramis oldugumuz sayi list icinde bulunmuyorsa fonksiyon geriye -1 donduruyor.

dizi = []
for x in range (0,100): # for dongusu yardimiyla dizimize 100 tane sayi ekliyoruz.
    dizi.append(random.randint(0,100)) # Bu sayilar dongunun her iterasyonunda 0-100 arasinda bulunan tam sayilardan rastgele olarak secilip list yapimiza append ediliyor(ekleniyor).

sayi = 16 # Aranan sayimizi 16 olarak belirliyoruz. Istediginiz gibi degistirebilirsiniz :) 
if lineer_arama(dizi,sayi) == - 1: # lineer_arama fonksiyonumuzun geriye dondurmus oldugu degere gore if-else yapimiz calisiyor
    print("Dizide aranan sayi bulunmamaktadir.\n")
else:
    print(f"Aranan sayi dizinin {str(lineer_arama(dizi,sayi))}. indisinde bulunmaktadir.\n" )

zaman_lineer = son_lineer - ilk_lineer # Algoritmanin calismaya basladigi andan sonlandigi ana kadar gecen zamani hesapliyoruz.
print(f"Calisma Suresi(Lineer Arama) = {zaman_lineer}\n")

son_program = time.time() # Programmin calisma suresini bulmak icin programin sonlandigi andaki sureyi bir degiskene kaydediyoruz
zaman_program = son_program - ilk_program # Programin calismaya basladigi andan sonlandigi ana kadar gecen zamani hesapliyoruz.
print(f"Calisma Suresi(Tum Program) = {zaman_program}\n")

# Not: Algoritmalarin ve programlarin calisma suresi BigO notasyonuyla(O(n)) tahmin edilebilmektedir.












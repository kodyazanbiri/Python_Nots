"""
Python'da çeşitli işlevler ve işlemler gerçekleştiren birkaç temel yöntemler:
String Methods (String Yöntemleri)
List Methods (Liste Yöntemleri)
Dictionary Methods (Sözlük Yöntemleri)
Set Methods (Küme Yöntemleri)
File Methods (Dosya Yöntemleri)
"""
#-------String Methods (String Yöntemleri)
upper() #Bir string'in tüm harflerini büyük harfe dönüştürür.
metin = "merhaba dünya"
buyuk_harf = metin.upper()
print(buyuk_harf)  # Çıktı: "MERHABA DÜNYA"

split() #Bir string'i belirtilen bir ayırıcıya göre bölerek bir liste döner.
metin = "Python programlama dili"
kelimeler = metin.split()
print(kelimeler)  # Çıktı: ['Python', 'programlama', 'dili']

#---------List Methods (Liste Yöntemleri)
append() #Bir listeye yeni bir öğe ekler.
liste = [1, 2, 3]
liste.append(4)
print(liste)  # Çıktı: [1, 2, 3, 4]

remove() #Belirtilen değere sahip ilk öğeyi listeden kaldırır.
liste = [1, 2, 3, 2]
liste.remove(2)
print(liste)  # Çıktı: [1, 3, 2]

#--------Dictionary Methods (Sözlük Yöntemleri)
get() #Belirtilen anahtarın değerini döner. Anahtar yoksa, varsayılan değeri döner.
sozluk = {"isim": "Ali", "yas": 25}
isim = sozluk.get("isim")
print(isim)  # Çıktı: Ali
meslek = sozluk.get("meslek", "Bilinmiyor")
print(meslek)  # Çıktı: Bilinmiyor

items()#Sözlükteki anahtar-değer çiftlerini bir liste olarak döner.
sozluk = {"isim": "Ali", "yas": 25}
elemanlar = sozluk.items()
print(elemanlar)  # Çıktı: dict_items([('isim', 'Ali'), ('yas', 25)])

#--------Set Methods (Küme Yöntemleri)
add() #Bir kümeye yeni bir öğe ekler.
kume = {1, 2, 3}
kume.add(4)
print(kume)  # Çıktı: {1, 2, 3, 4}

remove() #Bir kümeden belirli bir öğeyi kaldırır. Eğer öğe yoksa hata verir
kume = {1, 2, 3}
kume.remove(2)
print(kume)  # Çıktı: {1, 3}

#--------File Methods (Dosya Yöntemleri)
write() #Bir dosyaya veri yazar.
with open("ornek.txt", "w") as dosya:
    dosya.write("Merhaba Dünya!")

read() #Bir dosyadan veri okur.
with open("ornek.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)  # Çıktı: "Merhaba Dünya!"

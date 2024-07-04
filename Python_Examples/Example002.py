# 1- Bir öğrencinin aşağıdaki bilgileri için değişken oluşturunuz.

ogrenciAdi = 'Ayşe'
ogrenciSoyad = 'Kaya'
ogrenciAdSoyad = ogrenciAdi + ' ' + ogrenciSoyad
print(ogrenciAdSoyad)
ogrenciCinsiyet = False # Kadın
ogrenciOkulNumarasi = '20204567'
ogrenciDogumYili = 2004
ogrenciAdresi = 'Ankara Çankaya'
ogrenciYasi = 2024 - ogrenciDogumYili 

# Öğrenci bilgilerini yazdırma
print(f"Öğrenci Adı: {ogrenciAdi}")
print(f"Öğrenci Soyadı: {ogrenciSoyad}")
print(f"Öğrenci Ad + Soyad: {ogrenciAdSoyad}")
print(f"Öğrenci Cinsiyet: {'Kadın' if ogrenciCinsiyet == False else 'Erkek'}")
print(f"Öğrenci Okul Numarası: {ogrenciOkulNumarasi}")
print(f"Öğrenci Doğum Yılı: {ogrenciDogumYili}")
print(f"Öğrenci Adresi: {ogrenciAdresi}")
print(f"Öğrenci Yaşı: {ogrenciYasi}")

# 2- Aşağıdaki ders notlarının ortalamasını hesaplayınız.

# Ders notları
dersNotu1 = 85
dersNotu2 = 92
dersNotu3 = 78

# Ortalama hesaplama
ortalamaNot = (dersNotu1 + dersNotu2 + dersNotu3) / 3

# Ortalama notu yazdırma
print(f"Ortalama Not: {ortalamaNot:.2f}")

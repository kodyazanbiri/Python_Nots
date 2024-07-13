# 1-sayilar listesini while ile ekrana yazdırma:
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1

# 2-Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırma:
baslangic = int(input('Başlangıç: '))
bitis = int(input('Bitiş: '))

i = baslangic
while i < bitis:
    if i % 2 == 1:
        print(i)
    i += 1

# 3.soru: 1-100 arasındaki sayıları azalan şekilde yazdırma:
i = 100
while i > 0:
    print(i)
    i -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırma:
numbers = []
i = 0
while i < 5:
    sayi = int(input('Sayı: '))
    numbers.append(sayi)
    i += 1

numbers.sort()
print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler = []

adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0

while i < adet:
    name = input('Ürün ismi: ')
    price = input('Ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

i = 0
while i < len(urunler):
    urun = urunler[i]
    print(f'Ürün adı: {urun["name"]}, Ürün fiyatı: {urun["price"]}')
    i += 1


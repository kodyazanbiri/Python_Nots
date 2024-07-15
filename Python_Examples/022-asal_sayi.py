# Kullanıcıdan bir sayı girmesini isteyin
sayi = int(input('Bir sayı girin: '))
asalmi = True

# Eğer sayı 1 ise asal değildir
if sayi == 1:
    asalmi = False

# 2'den başlayarak sayının kendisine kadar olan sayıları kontrol edin
for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

# Sonucu ekrana yazdırın
if asalmi:
    print(f'{sayi} sayısı asaldır.')
else:
    print(f'{sayi} sayısı asal değildir.')

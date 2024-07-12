# Bir sayının 10 ile 20 arasında olup olmadığını kontrol edin
x = 15

result = 10 < x < 20
print(f'{x} sayısı 10 ile 20 arasında mı?: {result}')

# 2- and operatörünü kullanarak bir sayının pozitif olup olmadığını ve tek olup olmadığını kontrol edin
x = 7

result = (x > 0) and (x % 2 != 0)
print(f'{x} sayısı pozitif ve tek mi?: {result}')

# 3- or operatörünü kullanarak bir sayının 0'dan büyük veya 100'den küçük olup olmadığını kontrol edin
x = 105

result = (x > 0) or (x < 100)
print(f'{x} sayısı 0\'dan büyük veya 100\'den küçük mü?: {result}')

# 4- not operatörünü kullanarak bir sayının 5'ten küçük olup olmadığını kontrol edin
x = 3

result = not(x >= 5)
print(f'{x} sayısı 5\'ten küçük mü?: {result}')

# 5- Bir sayının 20 ile 30 arasında olup olmadığını ve çift olup olmadığını kontrol edin
x = 22

result = (20 < x < 30) and (x % 2 == 0)
print(f'{x} sayısı 20 ile 30 arasında ve çift mi?: {result}')

# 6- Bir sayının negatif olup olmadığını veya 50'den büyük olup olmadığını kontrol edin
x = -5

result = (x < 0) or (x > 50)
print(f'{x} sayısı negatif mi veya 50\'den büyük mü?: {result}')

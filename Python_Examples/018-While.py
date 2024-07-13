# 1'den 100'e kadar olan sayıları kontrol eden ve tek/çift olduğunu belirten kod
x = 1
while x <= 100:
    if x % 2 == 1:
        print(f'Sayı tek: {x}')
    else:
        print(f'Sayı çift: {x}')
    x += 1

print('Bitti...')

# Kullanıcının adını boş bırakmadığından emin olan kod
name = ''  # False
while not name.strip():  # Kullanıcı adı sadece boşluk karakterlerinden oluşuyorsa döngü devam eder
    name = input('İsminizi giriniz: ')

print(f'Merhaba, {name}')

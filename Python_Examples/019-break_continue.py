# 1'den 10'a kadar sayıları yazdırır ve x değeri 5 olduğunda döngüyü sonlandırır (break).
x = 0

while x < 10:
    x += 1
    if x == 5:
        break  # x değeri 5 olduğunda döngüyü sonlandırır
    print(x)

# 1'den 10'a kadar sayıları yazdırır. x değeri 5 olduğunda, bu değeri atlar (continue), ve x değeri 8 olduğunda döngüden çıkar (break).
x = 0

while x < 10:
    x += 1
    if x == 5:
        continue  # x değeri 5 olduğunda bu adımı atlar
    if x == 8:
        break  # x değeri 8 olduğunda döngüyü sonlandırır
    print(x)

# 1'den 100'e kadar olan tek sayıların toplamını hesapla
x = 1
result = 0

while x <= 100:    
    if x % 2 != 0:  # Eğer x tek sayıysa
        result += x
    x += 1

print(f'Toplam: {result}')

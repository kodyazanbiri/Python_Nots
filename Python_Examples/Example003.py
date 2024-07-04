#ornek1-------------
# Kullanıcıdan iki sayı al
x = input('1. sayı: ')
y = input('2. sayı: ')

# String olarak toplama
toplam_str = x + y
print("String olarak toplama sonucu:", toplam_str)  # Çıktı x ve y yanyana yazılır

# Sayısal toplama için tip dönüşümü yapmalıyız
toplam_int = int(x) + int(y)
print("Sayısal olarak toplama sonucu:", toplam_int)

# Tüm tip dönüşümlerini yapalım-------------
x = 5               # int
y = 2.5             # float
name = 'Ayse'       # str
isOnline = True     # bool

# int x için tip dönüşümleri
x_to_float = float(x)
x_to_str = str(x)
x_to_bool = bool(x)

print("x to float:", x_to_float)
print("x to str:", x_to_str)
print("x to bool:", x_to_bool)

# float y için tip dönüşümleri
y_to_int = int(y)
y_to_str = str(y)
y_to_bool = bool(y)

print("y to int:", y_to_int)
print("y to str:", y_to_str)
print("y to bool:", y_to_bool)

# str name için tip dönüşümleri
# int ve float dönüşümleri sadece sayısal stringlerde mümkündür, bu yüzden 'Ayse' dönüştürülemez
# Ancak, örnek olması açısından '123' gibi bir string kullanabiliriz
name_numeric = '123'
name_to_int = int(name_numeric)
name_to_float = float(name_numeric)
name_to_bool = bool(name)

print("name to int (numeric):", name_to_int)
print("name to float (numeric):", name_to_float)
print("name to bool:", name_to_bool)

# bool isOnline için tip dönüşümleri
isOnline_to_int = int(isOnline)
isOnline_to_float = float(isOnline)
isOnline_to_str = str(isOnline)

print("isOnline to int:", isOnline_to_int)
print("isOnline to float:", isOnline_to_float)
print("isOnline to str:", isOnline_to_str)

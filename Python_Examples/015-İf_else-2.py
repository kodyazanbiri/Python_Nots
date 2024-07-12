# Kullanıcıdan iki sayı girişi alınır
a = int(input('a: '))
b = int(input('b: '))

# a ve b karşılaştırılır
if a < b:
    print('a b\'den küçük')
elif a == b:
    print('a b\'ye eşit')
else:
    print('a b\'den büyük')

# Kullanıcıdan bir sayı girişi alınır
num = int(input('sayı: '))

# Sayı pozitif, negatif veya sıfır olup olmadığı kontrol edilir
if num % 2 == 0:
    print('sayı çift')
else:
    print('sayı tek')

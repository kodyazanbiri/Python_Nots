# range fonksiyonu örnekleri:

# 50'den başlayarak 100'e kadar (100 dahil değil) 20 adım aralığıyla sayıları yazdırır.
print("Range ile 50'den 100'e kadar 20 adım aralıkları:")
for item in range(50, 100, 20):
    print(item)

# 5'ten başlayarak 100'e kadar (100 dahil değil) 10 adım aralığıyla sayıları içeren bir liste oluşturur.
range_list = list(range(5, 100, 10))
print("\nRange ile oluşturulan liste:")
print(range_list)

# enumerate fonksiyonu
"""
enumerate, Python'da genellikle bir dizi veya iterable (örneğin liste, tuple, string gibi)
üzerinde döngü yaparken kullanılır. enumerate fonksiyonu, iterable'ın her bir öğesini alır ve bu öğeleri indeksi(konumunu)
ile birlikte döndürür.
"""
greeting = 'Hello'

# Bir diziyi (string) enumerate ile indeks ve öğe olarak yazdırır.
print("\nEnumerate ile indeks ve harfleri yazdırma:")
for index, letter in enumerate(greeting):
    print(f'Index: {index}, Letter: {letter}')


# zip fonksiyonu
"""
zip fonksiyonu, Python'da genellikle bir veya daha fazla iterable'ı (liste, tuple, string vb.) 
birleştirmek için kullanılır. zip fonksiyonu, her iterable'ın aynı indeksli öğelerini gruplayarak bunları bir tuple olarak döndürür.
"""

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

# Üç listeyi zip ile birleştirir ve her listedeki aynı indeksli öğeleri bir tuple olarak döner.
zipped_lists = list(zip(list1, list2, list3))
print("\nZip ile birleştirilen listeler:")
print(zipped_lists)

# Zip ile birleştirilen listeleri ayrı ayrı yazdırır.
print("\nZip ile birleştirilen listelerin öğelerini yazdırma:")
for item in zip(list1, list2, list3):
    print(item)

# Zip ile birleştirilen listelerin öğelerini ayrıştırarak yazdırır.
print("\nZip ile birleştirilen listelerin öğelerini ayrıştırarak yazdırma:")
for a, b, c in zip(list1, list2, list3):
    print(a, b, c)

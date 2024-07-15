#------Liste Comprehension: yeni bir liste oluşturmak için kullanılan bir sentakstır.
#0'dan 9'a kadar olan sayıların karelerini içeren bir liste oluşturma
kareler = [x**2 for x in range(10)]
print(kareler)
# Çıktı: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#-------Set Comprehension: yeni bir set oluşturmak için kullanılır.
# 0'dan 9'a kadar olan sayıların karelerini içeren bir set oluşturma
kareler_set = {x**2 for x in range(10)}
print(kareler_set)
# Çıktı: {0, 1, 64, 36, 4, 9, 16, 81, 49, 25}

#-------Dictionary Comprehension: yeni bir dictionary oluşturmak için kullanılır.
# 0'dan 9'a kadar olan sayıların karelerini içeren bir dictionary oluşturma
kareler_dict = {x: x**2 for x in range(10)}
print(kareler_dict)
# Çıktı: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#------Generator Comprehension: bir generator oluşturmak için kullanılır. Generator'lar bellekte yer kaplamaz, bunun yerine değerleri gerektiğinde üretir.
# 0'dan 9'a kadar olan sayıların karelerini içeren bir generator oluşturma
kareler_gen = (x**2 for x in range(10))
print(list(kareler_gen))
# Çıktı: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#-------Koşullu Comprehension: Comprehension'lar, koşullar ekleyerek daha karmaşık hale getirilebilir.
# 0'dan 9'a kadar olan çift sayıların karelerini içeren bir liste oluşturma
kareler_cift = [x**2 for x in range(10) if x % 2 == 0]
print(kareler_cift)
# Çıktı: [0, 4, 16, 36, 64]

# Liste ve demet (tuple) oluşturma
my_list = [1, 2, 3]
my_tuple = (1, 'iki', 3)

# Türlerini yazdırma
print(type(my_list))  # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>

# İkinci indekste bulunan elemanları yazdırma
print(my_list[2])  # 3
print(my_tuple[2])  # 3

# Uzunluklarını yazdırma
print(len(my_tuple))  # 3
print(len(my_list))  # 3

# List ve tuple'ı güncelleme
my_list = ['ali', 'veli']
my_tuple = ('damla', 'ayşe', 'ayşe')

# İki tuple'ı birleştirme
names = ('demet', 'emel', 'ayşe') + my_tuple
print(names)  # ('demet', 'emel', 'ayşe', 'damla', 'ayşe', 'ayşe')

# List'in ilk elemanını güncelleme
my_list[0] = 'ahmet'
# Tuple değiştirilemez, bu nedenle aşağıdaki satır yorum olarak kalmalıdır
# my_tuple[0] = 'deniz'

# Tuple içinde 'ayşe' kaç kez geçtiğini ve ilk görüldüğü indeksi bulma
print(my_tuple.count('ayşe'))  # 2
print(my_tuple.index('ayşe'))  # 1

# Güncellenmiş listeyi ve değiştirilemeyen tuple'ı yazdırma
print(my_list)  # ['ahmet', 'veli']
print(my_tuple)  # ('damla', 'ayşe', 'ayşe')

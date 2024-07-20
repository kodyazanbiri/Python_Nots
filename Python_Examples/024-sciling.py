"""
Python sciling işlemi:
Python'da bir veri yapısının (genellikle liste, dize veya tuple) belirli bir alt kümesini seçmek ve bu alt kümeyi elde etmek için kullanılan bir işlemdir.
Slicing işlemi, köşeli parantezler ([]) ve iki nokta üst üste (:) kullanılarak gerçekleştirilir. veri_yapisi[start:stop:step] şeklinde kullanılır. 
Slicing işlemi, Python'da veri manipülasyonu ve alt kümelerin elde edilmesi için oldukça güçlü ve kullanışlı bir yöntemdir.
"""
#------------listeler için slicing kullanımı
# Orijinal liste
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# İlk dört elemanı dilimleme
ilk_dort = liste[0:4]  # [0, 1, 2, 3]

# Beşinci elemandan (dahil) sona kadar dilimleme
besinci_sonra = liste[4:]  # [4, 5, 6, 7, 8, 9]

# Baştan altıncı elemana kadar (hariç) dilimleme
bas_altinci = liste[:5]  # [0, 1, 2, 3, 4]

# İkinci elemandan altıncı elemana kadar (hariç) dilimleme
ikinci_altinci = liste[1:5]  # [1, 2, 3, 4]

# Her ikinci elemanı dilimleme
her_ikinci = liste[::2]  # [0, 2, 4, 6, 8]

# Ters dilimleme
ters = liste[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#----------Dizeler için slicing kullanımı
# Orijinal dize
dize = "Python Dilimleme"

# İlk altı karakteri dilimleme
ilk_alti = dize[:6]  # 'Python'

# Yedinci karakterden sona kadar dilimleme
yedinci_sonra = dize[7:]  # 'Dilimleme'

# Belirli bir aralığı dilimleme
aralik = dize[7:14]  # 'Dilimle'

# Her ikinci karakteri dilimleme
her_ikinci = dize[::2]  # 'Pto ilee'

# Ters dilimleme
ters = dize[::-1]  # 'emelmilid nohtyP'

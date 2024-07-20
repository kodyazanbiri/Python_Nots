"""
Değer Tipi (Value Type):
name değişkeni bir değer tipidir. Stringler, tamsayılar gibi temel veri tipleri değer tipleri olarak kabul edilir.
Bu türler, fonksiyona argüman olarak geçirildiğinde, orijinal değişkenin bir kopyası geçirilir ve fonksiyon içindeki değişiklikler orijinal değişkeni etkilemez.
"""
def changeName(n):
    n = 'ada'

name = 'yiğit'

changeName(name)
print(name)  # yiğit

"""
Referans Tipi (Reference Type):
listeler referans tipidir. Listeler gibi karmaşık veri yapıları, fonksiyona argüman olarak geçirildiğinde, orijinal veri yapısının bir referansı (adresi) geçirilir.
Ancak sehirler[:] ile bir kopya geçirildiğinden, fonksiyon içindeki değişiklikler orijinal listeyi etkilemez.
"""
def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']

change(sehirler[:])

print(sehirler)  # ['ankara', 'izmir']

## BURDA KALDIMMMM------------

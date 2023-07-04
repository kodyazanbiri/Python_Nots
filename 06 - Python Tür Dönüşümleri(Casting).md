# Python Tür Dönüşümleri(Casting)
Programlamada birçok kez değişkenlerde tür dönüşümüne ihtiyaç duyulur. Örneğin string türündeki sayılarla (“5” veya “2” gibi) matematiksel işlem yapmamız 
gerektiğinde tür dönüşümü yapmamız gerekir. 

Python’ da Casting (tür dönüşümü) işlemi aşağıdaki fonksiyonlar kullanılarak yapılır.

`int()` , `float()` , `str()`

Örnek-1:

```python
x="5"
y=int("5")
 
print(x*2)# Ekranda 55 yazar
print(y*2)# Ekranda 10 yazar
```
Ekran Çıktısı:
```python
55
10
```

Örnek-2:
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#int'i float'a çevirmek:
a = float(x)

#float'ı int'e çevirmek:
b = int(y)

#int'i complex'e çevirmek:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

- Rastgele Sayı Oluşturmak

Python'da rastgele sayı elde edebilmek için random modülünün uygulamaya dahil edilmesi (import) gereklidir.

Örnek:
```python
import random

print(random.randrange(1, 10))    #örnekte Python'un 1 ile 10 arasında rastgele bir sayı seçmesi sağlanmıştır.
```
- random modülünün random() adlı fonksiyonunu kullanarak, 0.0 ile 1.0 arasında rastgele bir kayan noktalı sayı üretebilirsiniz.

Örnek:
```python
>>> random.random() # örneğin 0.8064301704207291 sayısını üretti
```
Örneğin:
- 0 ile 1 arası 10 tane sayı üretelim. Bu sayıları gösterirken de noktadan sonra yalnızca dört basamak görüntülenmesine izin verelim.
```python
for i in range(10):
    print("{:.4f}".format(random.random()))
"""
 0.3094
 0.5277
 0.1588
 0.2832
 0.8742
 0.9989
 0.6847
 0.5672
 0.5529
 0.9717   şeklinde sayılar üretebilir.
"""
```







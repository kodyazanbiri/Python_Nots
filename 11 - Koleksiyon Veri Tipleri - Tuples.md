# Koleksiyon Veri Tipleri - Tuples
Python'daki liste türlerinden bir diğeri tuple dir. Bir önceki derste anlatılan list'ten farklı olarak değiştirilemez, ilk tanımlandığı şekilde kalır. Bu dizelere ekleme, silme, sıra (index) değiştirme işlemi de yapılamaz.

İlk tanımlama yapılırken tuple nesnelerine parantez içinde yer verilir.

Örneğin:
```python
ornekTuple = ("muz", "elma", "kiraz")
print(ornekTuple)
```
### Tuple Değerleri Değiştirmek
Yukarıda bahsedildiği gibi tuple içindeki değerler değiştirilemez. Bu tarz bir işlem yapmak için öncelikle tuple list türüne dönüştürülmeli, ardından değişiklik yapıldıktan sonra yeni bir tuple oluşturulmalıdır:

Örneğin:
```python
x = ("muz", "elma", "kiraz")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

### Tek Elemanlı Tuple Oluşturmak
Eğer tuple türü dizemiz içinde tek bir eleman olacaksa tanımlarken ilk nesneden sonra virgül kullanılmalıdır. Bu kullanılmazsa string türde bir değişken elde edilmiş olur.

Örneğin:
```python
#Bir tuple:
thistuple = ("elma",)
print(type(thistuple))

#Bir tuple degil, bir string:
thistuple = ("elma")
print(type(thistuple))
```

### Birden Fazla Tuple Birleştirmek
Bu işlem için iki tuple artı (+) işareti ile toplanarak her iki dizeyi içeren yeni bir tuple elde edilebilir.

Örneğin:
```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

### Yapıcı (Constructor) Kullanarak Tuple Oluşturmak
Alışılagelmiş ("a", "b" , "c") yapısı yerine tuple() nesnesini kullanarak tuple oluşturulabilir.

Örneğin:
```python
ornekTuple = tuple(("elma", "muz", "kiraz")) # iki parantezli olduğunu unutmayın
print(ornekTuple)   # NOT: tuple'ın eleman sayısını elde etmek için len() fonksiyonu kullanılabilir.
```


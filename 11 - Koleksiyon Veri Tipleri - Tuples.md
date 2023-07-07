# Koleksiyon Veri Tipleri - Tuples
Tuple değiştirilemez, ilk tanımlandığı şekilde kalan bir veri tipidir. Bu dizelere ekleme, silme, sıra (index) değiştirme işlemi yapılamaz.

- İlk tanımlama yapılırken tuple nesnelerine parantez içinde yer verilir.

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
print(x)  # x adlı tuple y adlı listeye dönüştürüldü. Ardından 1. eleman "kiwi" olarak değiştirilmiş. Sonra liste tekrar tuple türüne dönüştürülmüş.
```

### Tek Elemanlı Tuple Oluşturmak
Eğer tuple veri tipinin içinde tek bir eleman olacaksa tanımlarken ilk nesneden sonra virgül kullanılmalıdır. Bu kullanılmazsa string türde bir değişken elde edilmiş olur.

Örneğin:
```python
#Bir tuple:
tuple1 = ("elma",)
print(type(tuple1))

#Bir tuple degil, bir string:
tuple1 = ("elma")
print(type(tuple1))
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
tuple() nesnesini kullanarak tuple oluşturulabilir.

Örneğin:
```python
ornekTuple = tuple(("elma", "muz", "kiraz")) # iki parantezli olduğunu unutmayın
print(ornekTuple)   # NOT: tuple'ın eleman sayısını elde etmek için len() fonksiyonu kullanılabilir.
```


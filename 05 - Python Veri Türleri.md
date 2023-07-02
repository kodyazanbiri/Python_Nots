# Python Veri Türleri
Değişkenler farklı türlerde veriler barındırabilir.
- Python'da varsayılan veri türleri tabloda gösterilmiştir:

|                         | Python Veri Tipleri      |
| --                      |  :-------                | 
|Metin(Text Type)         |     str                  |
|Sayı(Numeric Types)      |  int, float, complex      |
|Dize-Seri(Sequence Types)|  list, tuple, range | 
|Haritalama(Mapping Type) |  dict |
|Atama(Set Types)         |    set, frozenset   |
|Mantıksal(Boolean Type)  |    bool   |
|İkili(Binary Types)      |    bytes, bytearray, memoryview  |   

- Veri Türünü Tespit Etmek

Bunun için `type(değişken)` fonksiyonu kullanılır.

Örneğin:

```python
x = 5
print(type(x))
```
Çıktı:

```python
<class 'int'>
```
- Zincirleme atama(Chained Assignment)
 
Örneğin:
```python
>>> a = b = c = 300
>>> print(a, b, c)
300 300 300
```

- Print fonksiyonunda `"*"` kullanarak, verilen listenin dönmesi sağlanabilir.

Örneğin:
```python
>>> print(*'Python', sep = ".")
P.y.t.h.o.n

>>> a = [1,2,3,4]
>>> print(*a, sep=".")
1.2.3.4
```




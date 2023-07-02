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
### Sayısal Veri Tipleri

- Python'da üç sayısal tür bulunur:

  * int
  * float
  * complex
  
Değişken tanımlandığı zaman tanımlanan sayıya göre bu türlerden hangisi olacağı belirlenir.

Örneğin:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```
- İnt

Int bir tam sayı değeridir. Pozitif veya negatif bir sayı olabilir. Ondalıklı değer alamaz. Sonsuz uzunlukta olabilir.

Örneğin:

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```
- Float

Float, pozitif ya da negatif kesirli ve ondalıklı ifadeler barındırabilir.

Örneğin:

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```
- Complex

Complex, karmaşık sayıları ifade eder. Tanımlanırken j harfi ile belirtilir.

Örneğin:

```python

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```
### DİP NOT:
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




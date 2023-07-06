# Python Lambda
Python'da lambda, tek satırlık fonksiyonlardır. Bir ya da daha fazla parametre kabul ederler, ancak tek bir işlem yapabilirler. Aşağıdaki örnekte tanımlanan x fonksiyonu, parametrede belirtilen sayıya 10 ekler ve sonucu döndürür.

Örneğin:
```python
x = lambda a : a + 10
print(x(5))
```
- lambda, birden fazla parametreyi kabul eder. Aşağıda iki parametreli bir örnek verilmiştir:

Örneğin:
```python
topla = lambda a, b : a + b
print(topla(5, 6))
```
### Neden Lambda Fonksiyon Kullanmalıyız?
Bir fonksiyon içinde kullanıldığı zaman o fonksiyonu kişiselleştirmemizi sağlar. Bu durumu örnek üzerinden anlatalım. Örneği inceleyin:

Örneğin:
```python
def carp(n):
  return lambda a : a * n

carpan = carp(2)

print(carpan(11))
```
- Yukarıdaki örnekte carpan ifadesi kendisine verilen sayıyı 2 ile çarpan bir fonksiyona dönüşmüştür. Bu şekilde carpan(11) yazıldığında 22 sonucunu verir duruma gelir. Temel fonksiyon olan carp, farklı fonksiyonlar yaratmak için kullanılabilir.

Örneğin:
```python
def carp(n):
  return lambda a : a * n

ikiIleCarp = carp(2)
ucIleCarp = carp(3)

print(ikiIleCarp(11))
print(ucIleCarp(11))
```

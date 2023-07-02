# Boolean Veri Tipi
Python, iki veriyi değerlendirerek ifadenin doğru ya da yanlış olduğunu tespit eder. `True` ve `False` olmak üzere iki değeri vardır.

Python dilinde boolean ifadeler sayısal olarak `1` ve `0`'a tekabül eder. Sayısal ifadelerle yapılan tüm işlemler boolean ifadeler için de geçerlidir.

Örneğin:
```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
```
Çıktı:
```python
True
False
False
```
- Her zaman IF deyimi içerisinde bir koşul belirtilir. Koşulun gerçekleşme durumuna göre doğru ya da yanlış değeri döner.

Örneğin:
```python
a = 200
b = 33

if b > a:
  print("b, a'dan büyüktür")
else:
  print("b, a'dan büyük değildir")
```

- Python, değerlendirme işlemi için birçok fonksiyon içerir. Örneğin `isinstance()` bir değişkenin türünün belirtilen olup olmadığını tespit etmeye yarar.
Parantez içinde belirtilen ilk değer değişkenimizdir, ikinci belirtilen ise türdür. Değişken belirttiğimiz türde ise True, aksi takdirde False döner.

Örneğin:
```python
x = 200
print(isinstance(x, int))
```








# While Döngüsü
Python'da Döngüler
- Python, iki temel döngü yapısına sahiptir:
  * while Döngüsü
  * for Döngüsü
### while Döngüsü
Bir koşul gerçekleşene kadar while kod bloğundaki kodlar tekrar tekrar çalıştırır.

Örneğin:
```python
i = 1
while i < 6:
  print(i)
  i += 1
```
Yukarıda paylaştığımız kod çalıştırıldığı zaman i, 6'dan küçük olduğu sürece ekrana i'yi yazdırır ve i'yi bir arttırır. i'yi arttırmayı unutmayın! Aksi takdirde koşul gerçekleşemez ve while döngüsü hiç sonlanmaz.

while'ın sonlanmasını sağlayan koşul ifadesinde önceden tanımlanmış değişkenlere ihtiyaç duyarız. Bu nedenle while öncesinde i = 1 şeklinde bir tanımlama yaptık.

- Break Deyimi while çalıştırılırken bazen koşulu beklemeden döngüyü sonlandırmak gerekir. break döngüyü sonlandırmak için kullandığımız ifadedir.

Örneğin:
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```
Yukarıdaki örnekte i == 3 olunca while sonlanacak ve i hiçbir zaman 4 ya da 5 olamayacaktır.

### continue Deyimi
while kod bloğundaki işlemleri sonlandırıp döngüyü başa almak için kullanılır. Bu ifadeyi kullandığımız an döngü başa dönecek ve bu koddan sonraki satırlar çalışmayacaktır.

Örneğin:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```
Yukarıdaki örnekteki kod çalıştırılırsa while 3 olduğunda başa döndüğünü, bu nedenle ekrana "3" yazdırılmadığını görürüz:

Çıktı:
```python
 Görünüm
1
2
4
5
6
```
### else Deyimi
while döngüsü sonlandıktan sonra yapılacak işleri else ifadesi ile belirtebiliriz.

Örneğin:
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("Artık i, 6'dan küçük değil!")
```

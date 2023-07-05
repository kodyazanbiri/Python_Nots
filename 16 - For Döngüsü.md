# Python For Döngüsü
Python'da döngülerden biri de for döngüsüdür. Bu döngü, bir dizedeki (list, tuple, dict, set) veya metindeki (string) elemanları/harfleri tek tek ele alır.

Elbette for birçok programlama dilinde yineleyici işlevine sahiptir. Ancak python'da çok daha geniş bir kullanım olanağı sunar.

Örneğin:
```python
meyveler = ["muz", "elma", "kiraz"]
for x in meyveler:
  print(x)
```
Python'da for döngüsü önceden bir değişken tanımlamayı veya dize sırası (index) belirtmeyi gerektirmez.

### Metinleri Harf Harf Sıralamak
Tüm metin (string) türü değişkenler for kullanılarak harf harf sıralanabilir. Çıkan sonuç yine string olacaktır.

Örneğin:
```python
for x in "coğrafya":
  print(x)
```
- break İfadesi
Bu ifadeyi kullanarak for döngüsünü elemanların bitmesini beklemeden sonlandırabiliriz.

Örneğin:
```python
meyveler = ["elma", "portakal", "mandalina"]
for x in meyveler:
  print(x)
  if x == "portakal":
    break
```
### continue İfadesi
Bu ifadeyi kullanarak şimdiki yinelemeyi sonlandırabilir ve bir sonraki yineleme ile devam edebiliriz.

Örneğin:
```python
meyveler = ["elma", "portakal", "mandalina"]
for x in meyveler:
  if x == "portakal":
    continue
  print(x)
```
Yukarıdaki kod çalıştırıldığında ekrana "portakal" yazdırılmadığı görülecektir. Çünkü portakal ise continue kullandık ve o yinelemeyi geçip bir sonrakinden devam etmesini söyledik.

### range İfadesi
Belli sayıda tekrarlı bir döngü oluşturacaksak range(sayı) kodu kullanılabilir.

Örneğin:
```python
for x in range(6):
  print(x)
```
Yukarıdaki kod çalıştırıldığında derleyicinin ekrana 0'dan 5'e kadar sayılar yazdırdığı görülecektir.

- Eğer 0'dan değil de farklı bir sayıdan başlamasını istersek range(başla, git) kullanılabilir. İlk parametre hangi sayıdan başlayacağı, ikinci parametre kaça kadar gideceği (bu sayı dahil değildir) sayıdır.

Örneğin:
```python
for x in range(2, 6):
  print(x)
```
- range, varsayılan olarak birer birer artar. Ancak üçüncü parametrede artış miktarını belirtebiliriz. Örneğin 2'den 30'a kadar saydırmasını ve üçer üçer atlamasını istiyorsak aşağıdaki kod işimize yarayacaktır:

Örneğin:
```python
for x in range(2, 30, 3):
  print(x)
```
### else İfadesi
for döngüsü bittikten sonra yapılacakları, for'dan sonra kullanacağımız else ile belirtebiliriz:

Örneğin:
```python
for x in range(6):
  print(x)
else:
  print("Sonunda bitti!")
```
### İç İçe Döngüler
Döngü içinde döngü kullanabiliriz. Böyle ifadelerde içteki döngü, dıştaki döngü kadar tekrarlanır.

Örneğin:
```python
sinif = ["1","2","3"]
sube = ["A","B","C"]

for x in sinif:
   for y in sube:
      print(x, y)
```
### pass Deyimi
for döngüsünden sonra mutlaka kod yazılmalıdır. Eğer bu döngü çalıştırıldıktan sonra hiçbir kod çalıştırılmaması gerekiyorsa pass yazılarak döngü geçilebilir.

Örneğin:
```python
for x in [0, 1, 2]:
  pass
```

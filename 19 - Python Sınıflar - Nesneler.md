# Python Sınıflar - Nesneler
Python, nesne tabanlı bir programlama dilidir. Python'da neredeyse her şey bir sınıftır.

Bir sınıf (class), kendisinden örnek oluşturulabilen bir nesnedir (object). Bu sınıflara özellik ve yöntemler atanabilir.

### Bir Sınıf Oluşturmak
Sınıf oluşturmak için class ifadesi kullanılır. Bu ifadeden sonra sınıfın adına yer verilir ve iki nokta üst üste kullanılarak sınıf yapısı yazılmaya başlanır:

Örneğin:
```python
class Sinifim:
  x = 5
```
Yukarıdaki örnekte Sinifim adında ve tek özellikli (x) bir sınıf oluşturulmuştur.

### Sınıfın Bir Örneğini (Nesne) Oluşturmak
Yukarıdaki örnekte bir sınıf tanımladık. Peki bu sınıfı nasıl nesne olarak oluşturup kullanacağız? Bunun için aşağıdaki örneği inceleyin:

Örneğin:
```python
class Sinifim:
  x = 5

p1 = Sinifim()
print(p1.x);
```
Örnek kodu incelediğimizde, nesne yaratırken sınıf adını ve sonrasında parantez aç-kapat yapıyoruz.

### __init__() Fonksiyonu
Bundan önceki örnekler bir sınıfın temel bileşenleriydi. Şimdi bahsedilecek olan __init__() fonksiyonu ise sınıfın temel bileşenidir. Nesne oluşturulduğunda ilk olarak bu fonksiyon çalıştırılır.

Örneğin:
```python
class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

p1 = Kisi("Murat", 36)

print(p1.isim)
print(p1.yas)
```
Yukarıdaki örnekte def __init__(self, isim, yas): sınıfın yapıcı fonksiyonudur. Burada belirtilen isim ve yas değişkenleri, sınıfın bir örneği oluşturulurken kullanılan değişkenlerdir.

### Nesne Yöntemleri/Metotları
Nesneler için sınıfa özgü yöntemler/metotlar geliştirilebilir. Nesne yaratıldıktan sonra bu yöntemler .yontemAdi() şeklinde çalıştırılabilir.

Örneğin:
```python
class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas
  def yazdir(self):
    print("Merhaba, adım ", self.isim, ", yaşım ", self.yas);

p1 = Kisi("Murat", 36)
p1.yazdir()
```
NOT: Yukarıdaki örneklerde geçen self, sınıfın kendisini ifade eden bir parametre olup nesneye ait özellik ve yöntemlerle işlem yaparken kullanılır. İstenilirse bunun yerine farklı adlandırmalar yapılabilir. Ancak __init__() ve yöntemlerde kullanılması zorunludur. Aşağıdaki örnekte önce kendisi, sonradan da kisi şeklinde adlandırılıp kullanılmıştır:

Örneğin:
```python
class Kisi:
  def __init__(kendisi, isim, yas):
    kendisi.isim = isim
    kendisi.yas = yas
  def yazdir(kisi):
    print("Merhaba, adım ", kisi.isim, ", yaşım ", kisi.yas);

p1 = Kisi("Murat", 36)
p1.yazdir()
```
### Nesne Özelliklerini Değiştirmek
Nesne özelliğinden sonra eşittir yazılarak yeni değer ifade edilebilir:

Örneğin:
```python
class Kisi:
  def __init__(self, isim, yas):
    self.isim = isim
    self.yas = yas

p1 = Kisi("Murat", 36)
p1.yas = 40
print(p1.yas)
```
### Nesnenin Bir Özelliğini Ya Da Nesneyi Silmek
Bunun için del ifadesi kullanılabilir:

Örneğin:
```python
kisi = new Kisi("Murat", 36)

del kisi.yas # yas özelliğini siler

del kisi # nesneyi tamamen siler
```
### pass İfadesi
Sınıflar boş olamaz. En azından tek bir satırlık kod beklerler. Bu nedenle eğer hiçbir kod yazılmayacaksa sınıftan sonra pass yazılmalıdır.

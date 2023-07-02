# Python Değişkenleri
Değişkenler, herhangi bir veri içeren ifadelerdir. Diğer programlama dillerinden farklı olarak pythonda değişken önden tanımlanmaz. Değişken yazıldığı zaman ilk değer eklenir. Yani bir değişken bildirim komutu yoktur.

- Bir değişken ona değer atadığınız an oluşturulur. Örneğin,
```python
x = 2
y = "örnek bir yazı."
print(x)
print(y)
```

- Değişkenlerin herhangi bir türle bildirilmesi gerekmez ve ayarlandıktan sonra türü değiştirebilir. Örneğin,
```python
x = 4  # x int türünde tanımlandı
x = "Python" # Şimdi de x değişkenine string türü değer atandı.
print(x)
```
### Değişken İsimlendirme
Bir değişken kısa bir ada sahip olabilir (x ve y gibi) veya daha açıklayıcı bir isimde (yas, sayi,toplam) olabilir. 

- Python değişkenleri için kurallar:

  * Değişken adı, bir harfle veya alt çizgi karakteri ile başlamalıdır.
  * Bir değişken adı, bir sayıyla başlayamaz.
  * Bir değişken adı yalnızca alfa sayısal karakterler ve altçizgiler içerebilir (Az, 0-9 ve _)
  * Değişken isimler büyük küçük harf duyarlıdır (yaş, yaş ve YAŞ üç farklı değişkendir)
  * 
Örneğin:
```python
#Geçerli değişken adları
degisken = "örnek"
de_gisken = "örnek"
_de_gis_ken = "örnek"
deGisKen = "örnek"
DEGISKEN = "örnek"
degisken2 = "örnek"

#Kuraldışı değişken adları
2degisken = "örnek"
de-gis-ken = "örnek"
degis ken = "örnek"
```
### Değişkenlere Değer Atamak

- Birden Fazla Değişkene Aynı Anda Değeri Atamak.

Bunun için virgül ile ayrılarak değişkenler yazılır ve eşittir karşısına sırasıyla atanacak değerler yazılır.

Örneğin: 

```python
x, y, z = "Portakal", "Muz", "Kiraz"
print(x)
print(y)
print(z)
```

- Değişkenlere aynı değeri atamak da mümkündür.

Bunun için değişkenler arasına eşittir koyar ve son eşittirden sonra değeri yazarız.

Örneğin:

```python
x = y = z = "Portakal"
print(x)
print(y)
print(z)
```

### Değişkenleri / Metinleri Birleştirme

- Hem metni hem de bir değişkeni birleştirmek için, Python `“+” (artı)` karakterini kullanır.

Örnek:
```python
x = "Merhaba"
print("Dünya " + x)
```
- Artı (+) ifadesini değişkenleri birleştirmek için de kullanabiliriz.

Örneğin:
```python
x = "Merhaba"
y = "Dünya"
z =  x + y
print(z)
```
- Eğer iki sayısal ifade arasında artı (+) kullanırsak, buradaki artı toplama işlemini belirtir.

Örneğin:
```python
x = 5
y = 10
print(x + y)
```
### Yerel(Local) ve Genel(Global) Değişkenler !!! ANLAMADIM BUNU DÜZENLEEE

Yerel değişkenler sadece tanımlandıkları kod bloğunda tanımlıyken, genel (global) değişkenler ise kodlarımızın tamamında tanımlıdır.
Bir fonksiyonun dışında tanımlanmış tüm değişkenler genel (global) değişkenlerdir.

- Global değişkenler;

Global bir değişken, herhangi bir yerden erişilebilen bir değişkendir. Bir fonksiyonun dışında tanımlanan ve bildirilen ve herhangi bir yerde kullanılabilen değişkenlerdir.

Örneğin:

```python
x = "Dünya"

def myfunc():
  print("Merhaba " + x)

myfunc()
```




- Yerel değişkenler;

Fonksiyonlarda tanımlanan değişkenler yerel değişkenler olarak adlandırılır. Yerel değişkenlerle kastettiğimiz şey değişkenlerin fonksiyona özgü olması ve fonksiyonun işi bittikten sonra bellekten silinip kaybolmasıdır. Böyle değişkenlere başka bir yerden erişilemez.

Örneğin:

```python
def function():
    a = 5
   
function()
print(a)
```







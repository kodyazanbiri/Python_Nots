# Python Fonksiyonlar
Fonksiyonlar, sadece çağırıldıklarında çalışan kod parçalarıdır. Veri döndürebilirler.

Fonksiyonları çalıştırırken değişkenleri fonksiyona iletebilirsiniz. Biz bunlara parametre diyeceğiz.
Bir Fonksiyon Yaratmak
- Python'da fonksiyon yaratırken def kodu kullanılır.

Örneğin:
```python
def fonksiyonum():
  print("Bir fonksiyondan merhaba!")
```
Örnekte görüldüğü gibi def ifadesinden sonra fonksiyonun adına yer verilir (fonksiyonum). Parantez açılır, varsa parametreler yazılır ve parantez kapatılır. Ardından iki nokta koyularak fonksiyon çağırıldığında çalışması istenen kodlar yazılmaya başlanır.

### Bir Fonksiyonu Çağırmak
Fonksiyonu çalıştırmak için fonksiyonun adını yazın, ardından parantez açıp kapatın.

Örneğin:
```python
def fonksiyonum():
  print("Bir fonksiyondan merhaba!")

fonksiyonum()
Parametreler (Argümanlar)
```
- Fonksiyonlara bilgi parametreler vasıtasıyla iletilir.

Parametre, fonksiyon adından sonra parantez içinde belirtilir. Birden fazla parametre kullanılabilir. Bunlar virgül (,) ile ayrılır.

Aşağıdaki örnekte tek parametreli bir fonksiyon oluşturuldu. Fonksiyon çağırıldığı zaman, veri bu parametre sayesinde fonksiyona iletilecek.

Örneğin:
```python
def fonksiyonum(isim):
  print("Adınız: " + isim)

fonksiyonum("Murat")
fonksiyonum("Yasemin")
```
Örnek incelenirse, fonksiyon çağırırken parantez içinde "Murat" ifadesi kullandık. Bu veri fonksiyona "isim" adlı bir değişken olarak aktarıldı.

### Parametre Sayısı
Fonksiyonu oluştururken kaç parametre taşıyabileceği belirtilir. Fonksiyon çağırılırken bu sayıda parametre olması beklenir. Örneğin, fonksiyon iki parametre ile oluşturulduysa, çağırırken sadece iki parametre yazabiliriz demektir.

Örneğin:
```python
def fonksiyonum(ad, soyad):
  print("Adınız: " + ad + ", Soyadınız: " + soyad)

fonksiyonum("Murat", "Eliçalışkan")
```
Yukarıdaki örnekte iki değil de üç parametre yazsaydık, derleyici hata verirdi.

### Değişken Sayıda Parametre Alabilen Fonksiyonlar
Fonksiyonun kaç parametre alacağı ile ilgili kesin bir bilgi yoksa, bir veya daha fazla sayıda veriyi parametreden önce yıldız (*) koyarak almasını sağlayabilirsiniz. Bu şekilde fonksiyona iletilen bilgi tuple türünde bir dize olacaktır.

Örneğin:
```python
def fonksiyonum(*cocuklar):
  print("En genç çocuk: " + cocuklar[2])

fonksiyonum("Yağmur", "Mert", "Gamze")
```
### Parametre Anahtarları Kullanmak
Parametreleri, anahtar = değer şeklinde bir yapı ile göndermeniz mümkün. Bu durumda parametre sırası önemsizdir.

Örneğin:
```python
def fonksiyonum(cocuk3, cocuk2, cocuk1):
  print("En genç çocuk: " + cocuk3)

fonksiyonum(cocuk1 = "Yağmur", cocuk2 = "Mert", cocuk3 = "Gamze")
```
### İsteğe Bağlı Parametre Alan Fonksiyonlar
Bazen fonksiyonlara istenilen isim ve değerde değişken göndermek gerekebilir. Bunun için anahtar = değer yapısında değişkenler kabul eden fonksiyonlar yazılabilir. Yapılması gereken fonksiyon parametresinde değişkenin önüne iki yıldız (**) eklemektir:

Örneğin:
```python
def my_function(**cocuk):
  print("Soyadı " + cocuk["soyad"])

my_function(ad = "Tobias", soyad = "Smith")
```
### Varsayılan Parametre Değeri Belirtmek
Parametre gerektiren bir fonksiyonda parametre kullanılmadığı zaman geçerli olacak parametre değerini = değer şeklinde yazarak belirtebiliriz.

Örneğin:
```python
def nereden(ulke = "Türkiye"):
  print("Nereden: " + ulke)

nereden("İsveç")
nereden("Hindistan")
nereden()
nereden("Brezilya")
```
### Fonksiyona Parametre Olarak Bir Liste Göndermek
Metin, sayı, liste, sözlük vb. her türlü değişken parametre olarak talep edilebilir ve gönderilebilir. Örneğin bir listeyi (list) parametre olarak gönderirseniz, fonksiyon içine de o türde geçecektir:

Örneğin:
```python
def meyveler(food):
  for x in food:
    print(x)

meyveIsimleri = ["elma", "muz", "kiraz"]

meyveler(meyveIsimleri)
```
### Fonksiyondan Değer Döndürmek
Fonksiyonların çalıştıktan sonra bir değer döndürmesini return <deger> ifadesini kullanarak sağlayabiliriz.

Örneğin:
```python
def fonksiyonum(x):
  return 5 * x

print(fonksiyonum(3))
print(fonksiyonum(5))
print(fonksiyonum(9))
pass İfadesi
```
- Fonksiyonlar boş olamaz. En az bir satırlık kod içermelidir. Herhangi bir değer döndürmüyorsa pass kullanılmalıdır.

Örneğin:
```python
def fonksiyonum():
  pass
```
### Fonksiyon İçinde Kendisini Çağırmak
Python'da fonksiyonlar kendisini çalıştırabilir (recursion). Özellikle matematikte önemli bir yeri olan bu şekilde kullanımlarda dikkatli olmak lazım. Çünkü hata yapılırsa sonsuz döngüler oluşabilir ve bu da programın hem çalışmamasına hem de işlemciyi yormasına neden olur.

Örneğin:
```python
def topla(k):
  if(k > 0):
    result = k + topla(k - 1)
    print(result)
  else:
    result = 0
  return result

topla(6)
```
Yukarıdaki örnek çalıştırıldığı zaman belirtilen parametredeki sayıyı, bir küçük sayı ile toplar ve bu süreci k 0'dan büyük olduğu sürece yapar. Son yazan sonuç, o sayıya kadar olan sayıların toplamıdır.

- Başka bir örnek faktöriyel hesabıdır. Aşağıdaki fonksiyonda belirtilen sayı 1 oluncaya kadar çarpılır ve sonuç ekrana yazdırılır.

Örneğin:
```python
def faktoriyel(n):  
   if n == 1:  
       return n  
   else:  
       return n*faktoriyel(n-1)  

print(faktoriyel(4))
```

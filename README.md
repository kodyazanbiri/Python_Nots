# Python Temel Söz Dizimi
### 1. Python Tanımlayıcıları
Python tanımlayıcısı, bir değişken, fonksiyon, sınıf, modül veya başka bir nesneyi tanımlamak için kullanılan bir addır.

Tanımlayıcı, `A`’dan `Z`’ye veya `a`’dan `z`’ye veya `alt çizgi (_)`, ardından sıfır veya daha fazla harf, alt çizgi ve rakam (0’dan 9’a kadar) ile başlar.

Python, tanımlayıcılarda `@`, `$` ve `%` gibi noktalama karakterlerine izin vermez.

Python, büyük küçük harf duyarlı bir programlama dilidir. Örneğin, `temp` ve `Temp` iki farklı tanımlamayı temsil eder.

- Python tanımlama kuralları:
  * Sınıf isimleri büyük harfle başlar. Diğer tüm tanımlayıcılar küçük harfle başlar.
  * Tek bir önde gelen alt çizgi ile bir tanımlayıcıyı başlatmak, tanımlayıcının özel olduğunu gösterir.
  * İlk karakter sayı olamaz. Harf veya alt çizgi karakteri ile başlamalıdır.
  * Değişken adları büyük küçük harf duyarlıdır. X ile x farklı değişkenler olarak kullanılabilir.

### Python İçin Ayrılmış Kelimeler(Anahtar kelimeler)
|        |Python Anahtar Kelimeler                  | 
| --     |  :-------                                | 
| and    |  Mantıksal işlemci                       | 
| as     |  Bağlantı oluşturmak için kullanılır.    | 
| assert |  Hata ayıklama amacıyla kullanılır.      | 
| class  |  Sınıf bildirimi yapmak için kullanılır. |                                         |
|continue|  Bir döngüde bir sonraki tekrara doğrudan geçiş için kullanılır.|
| def    |  Bir fonksiyon tanımlamak için kullanılır. |
| del    |  Bir nesneyi silmek için kullanılır.     |
| elif   |  Koşula bağlı yapılarda kullanılır.      |
| else   |  Koşula bağlı yapılarda kullanılır.      |
| except |  Bir istisna meydana geldiğinde, yapılacak.|
| finally|  İstisnalar ile birlikte kullanılır ve bir istisna meydana gelip gelmediğine bakılmaksızın çalışan kodları gösterir|
| for    |  Bir for döngüsü oluşturmak için kullanılır |
| from   |  Bir modülün belirli parçalarını almak için kullanılır. |
| global |  Global bir değişken tanımlamak için kullanılır. |
|  if    |  Koşula bağlı bir yapı tanımlamak için kullanılır.|
|import  |  Bir modül almak için kullanılır. |
|  in    |  Bir değişkenin bir listede yer alıp almadığını kontrol etmek için kullanılır.|
|   is   |  İki değişkenin eşit olup omadığını belirlemek için kullanılır. |
| lambda |  Anonim bir fonksiyon oluşturmak için kullanılır. |
| none   |  Null bir değeri temsil eder.  |
| non    |  local Lokal olmayan bir değişken tanımlar.  |
| not    |  Mantıksal bir işlemcidir.        |
| or     |  Mantıksal bir işlemcidir.                                   |
| pass   |  Null bir ifadedir. Hiç bir işlem yapmaz                     |
|raise   |  Bir istisna tanımlar.                     |
| return |  Bir fonksiyondan çıkış yapar ve bir değer geri döndürür.    |
| true   |  Karşılaştırma işlemlerinde doğru değeri gösterir.   |
| try    |  Bir try...except yapısı tanımlar.          |
|  while |  Bir while döngüsü oluşturmak için kullanılır.           |
| with   |İstisna işlemini kolaylaştırmak için kullanılır. |
| yield  |  Bir fonksiyonu sona erdirir ve bir generator geri döndürür. |







### 1. Satırlar, Girinti ve Boşluklar
Birçok programlama dilinde sınıf tanımları, fonksiyon tanımları ve akış kontrolü için kod blokları oluşturulurken parantez kullanılır. Fakat python'da bu durum biraz farklıdır.
Python parantez yerine girinti şeklinde kod bloklarını alır. Girintideki boşluk sayısı kod bloğuna göre değişkenlik gösterir.
- Örneğin aşağıdaki kullanım doğru bir kullanımdır.
```python
if 2 > 1:
   print("iki, bir'den büyüktür.")
```
- Yukarıdaki kullanım şekline dikkat edin. Eğer aşağıdaki gibi bir kullanım yaparsanız hata alırsınız.
```python
if 2 > 1:
print("iki, bir'den büyüktür.")       #sözdizimi hatası
```
- Kaç tane boşluk olacağı tamamen isteğe bağlıdır.
```python
if 2 > 1:
  print("iki, bir'den büyüktür") 
if 2 > 1:
    print("iki, bir'den büyüktür")
```
- Her kod bloğunda aynı sayıda boşluk olmalıdır. Farklı sayıda boşluklar varsa hata verir.
```python
if 2 > 1:
  print("iki, bir'den büyüktür")
     print("iki, bir'den büyüktür")
```

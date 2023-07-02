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

### 2. Python İçin Ayrılmış Kelimeler(Anahtar kelimeler)
Python için tanımlanmış anahtar kelimeler mevcuttur. Bu kelimeleri değişken ve fonksiyon tanımlamalarında kullanamıyoruz. Bu durum diğer programlama dilleri için de söz konusudur.

Python'da anahtar kelimelerde büyük küçük harf duyarlılığı vardır. Bütün anahtar kelimeler küçük harf ile yazılır burada True, False ve None anahtar kelimeleri istisna oluşturmaktadır(Bunlar büyük harfle başlar).

Aşağıda Python'da kullanılan anahtar kelimelerin tablosu verilmiştir.

|        |Python Anahtar Kelimeler                  | 
| --     |  :-------                                | 
| True   | Karşılaştırma işlemlerinde doğru değeri gösterir. |
| False  | Karşılaştırma işlemlerinde yanlış değeri gösterir.|
| None   |  Null bir değeri temsil eder.  |
| and    |  Mantıksal işlemci                       | 
| as     |  Bağlantı oluşturmak için kullanılır.    | 
| assert |  Hata ayıklama amacıyla kullanılır.      | 
| class  |  Sınıf bildirimi yapmak için kullanılır. |                                         |
|continue|  Bir döngüde bir sonraki tekrara doğrudan geçiş için kullanılır.|
| def    |  Bir fonksiyon tanımlamak için kullanılır. |
| del    |  Bir nesneyi silmek için kullanılır.     |
| elif   |  Koşula bağlı yapılarda kullanılır.      |
| else   |  Koşula bağlı yapılarda kullanılır.      |
| except |  Bir istisna meydana geldiğinde, yapılacak işlemi tanımlamak içn kullanılır.|
| finally|  İstisnalar ile birlikte kullanılır ve bir istisna meydana gelip gelmediğine bakılmaksızın çalışan kodları gösterir|
| for    |  Bir for döngüsü oluşturmak için kullanılır |
| from   |  Bir modülün belirli parçalarını almak için kullanılır. |
| global |  Global bir değişken tanımlamak için kullanılır. |
|  if    |  Koşula bağlı bir yapı tanımlamak için kullanılır.|
| import |  Bir modül almak için kullanılır. |
|  in    |  Bir değişkenin bir listede yer alıp almadığını kontrol etmek için kullanılır.|
|   is   |  İki değişkenin eşit olup omadığını belirlemek için kullanılır. |
| lambda |  Anonim bir fonksiyon oluşturmak için kullanılır. |
| non    |  local Lokal olmayan bir değişken tanımlar.  |
| not    |  Mantıksal bir işlemcidir.        |
| or     |  Mantıksal bir işlemcidir.                                   |
| pass   |  Null bir ifadedir. Hiç bir işlem yapmaz                     |
| raise  |  Bir istisna tanımlar.                     |
| return |  Bir fonksiyondan çıkış yapar ve bir değer geri döndürür.    |
| try    |  Bir try...except yapısı tanımlar.          |
| while  |  Bir while döngüsü oluşturmak için kullanılır.           |
| with   |İstisna işlemini kolaylaştırmak için kullanılır. |
| yield  |  Bir fonksiyonu sona erdirir ve bir generator geri döndürür. |


### 3. Satırlar, Girinti ve Boşluklar
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
### 4. Tırnak kullanımı
Çoğu programlama dilinde string ifadeleri tırnak içine alınır. Python, `tek (‘)`, `çift (“)` ve `üçlü (""")` tırnakları kabul eder. Üçlü tırnaklar, dizgiyi birden çok satıra yaymak için kullanılır. 

Örneğin, aşağıdakilerin kodların tümü çalışır.
```python
kelime = 'kelime'
cumle = "Bu bir cümledir."
paragraf = """Bu bir paragraftır.
Birden fazla satır veya cümleden oluşmuştur."""
```
### 5. Yorum Yazma
Yazdığımız kodları, oluşturduğumuz algoritmaları tekrar bizim veya bir başkasının rahat bir şekilde anlaması için yorum yazmanızda gerekmektedir.
Python dili `#` karakterini yoruma başlamak için kullanır. Yazdığımız kodlar yorumlanırken bu karakter sonrası ta ki enter karakterine kadar dikkate alınmaz. 
Enter bir karakterdir. Enter tuşuna bastığınızda `“\n”` gibi ama çoğu editörde gösterilmeyen bir karakter oluşur. ASCII tablosuna bakacak olursanız enter karakterinin ASCII karşılığına da görebilirsiniz. 

### 6. Tek bir satıra birden fazla ifade yazma
C, C#, Java, Javascript gibi dillerde bir ifade “;” ile bitirilir. Ancak Python’da enter tuşuna basmanız ifadenin bittiği anlamına gelir. Peki birden fazla ifadeyi tek satıra nasıl yazarız? Bunun için `“;”` ihtiyaç vardır. Tek satır için tüm ifadelerinizi “;” ile birbirinden ayırabiliriz. 

Örneğin:
```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```
### 7.  Kod bloğuna başlama “:”
Bir grup ifadeyi while, if, def ve sınıf gibi ifadelerden sonra bir başlık satırı, iki nokta üs üste `(:)` den sonra kod bloğu gelir.

Örneğin:
```python
if ifade1 : 
   suite
elif ifade2 : 
   suite

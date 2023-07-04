# Python String Değişkenler
Python'da string (metin, yazı vb.) ifadeler tırnak `(")` ya da üst ayraç `(')` işareti arasında tanımlanmış ifadelerdir. Bir harften ya da harfler dizisinden oluşabilir.

Bu tarz değişkenleri `print()` fonksiyonu kullanarak ekrana yazdırabilirsiniz.

Örneğin:

```python
print("Merhaba")
```

### Bir Değişkene String Değer Atamak

Örneğin:

```python
a = "Merhaba"
print(a)
```
### Çok Satırlı Değer Yazmak

Art arda `üç tırnak ("""""")` kullanarak birden fazla satır içeren değerler yazabiliriz. İfadeyi tamamlamak için yine üç tırnak kullanırız.

Örneğin:

```python
a = """Burada
birkaç satırlı bir
değişken görüyorsunuz!"""
print(a)   # üç tane üst ayraç (''') da kullanılabilir.
```

### String Aynı Zamanda Bir Harf Dizisidir
Birçok programlama dilinde olduğu gibi Python dilinde de string değerler harfleri ifade eden küçük parçalara ayrılırlar. Ancak Python, C# daki gibi char değişkenine sahip değildir. Sonuçlar da string olacaktır.

String dizisindeki bir elemana ulaşmak için köşeli parantezden faydalanılır.

Örneğin:

```python
a = "Merhaba Dünya!"
print(a[1])   # e harfini verir
```

### Metnin Bir Kısmını Elde Etmek

Bir string ifadenin belli bir kısmını alabilirsiniz. Bunun için köşeli parantez içinde kesme işleminin başlayacağı pozisyonu ve kaç karakter alınacağı belirtilmelidir.

Örneğin:

```python
b = "Merhaba Dünya!"
print(b[2:5])  #çıktı: rha olur 
```
Kod çalıştırıldığı zaman derleyici ekrana rha yazdıracaktır. r harfi dizinin 2. elemanıdır (ilk eleman 0 ile belirtilir). İki noktadan sonra belirtilen 5 ise kaçıncı
pozisyona kadar eleman ekleneceğidir. 5 dahil değildir. Bu durumda r = 2, h = 3, a = 4 olduğu için uygulama rha şeklinde bir çıktı verecektir.

### String Karakter Uzunluğunu Bulmak

`len()` fonksiyonu ile bir string değerin kaç karakterden oluştuğunu elde edebiliriz.

Örneğin:

```python
a = "Merhaba Dünya!"
print(len(a))   # 14
```
### String Fonksiyonları (Metotları)
- Bu fonksiyonlar:
  * strip() Metodu
  * len() Metodu
  * lower() Metodu
  * upper() Metodu
  * replace() Metodu
  * split() Metodu
  * input() Metodu

### 1. strip() Metodu
Bu method metinde bulunan boşlukları kaldırır. Başta ve sonda boşluklar varsa bu boşlukları kaldırır.

Örneğin:
```python
a = " Merhaba Dünya   "
print(a.strip()) # Ekranda "Merhaba Dünya" yazacaktır.
```
- strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.

Örneğin:
```python
name = ",,,,...!!suna***"
x = name.strip(',.!*')
print("my name is " +  x)  # my username is suna
```
### 2. len() Metodu
Bu metot metnin uzunluğunu geri döndürecektir.

Örneğin:

```python
 
a = "Merhaba"
print(len(a))  # Ekranda 7 yazacaktır.
```
### 3. lower() Metodu
Bu metot çalıştırılarak string değişkendeki tüm karakterlerin küçük harfe dönüştürülmesi sağlanır.

Örneğin:

```python
a = "PytHon ÖRNEKleri"
print(a.lower())  # Ekranda ‘python örnekleri‘ yazacaktır.
```

### 4. upper() Metodu
upper() metodu lower() metodunun tam tersi olarak çalışır. Yani metindeki harflerin tümünü büyük harfe çevirir. Bir stringte tümü büyük harfe çevrilmek 
istenen metin varsa upper() metodu kullanılır.

Örneğin:

```python
a = "PytHon ÖRNEKleri"
print(a.lower())   # Ekranda ‘PYTHON ÖRNEKLERİ‘ yazacaktır.
```

### 5. replace() Metodu
Replace metodu karakter güncellemesi için kullanılır. 

Örneğin:
```python
a = "Python Örnekleri"
print(a.replace("e", "*"))   # Ekranda ‘Python Örn*kl*ri‘ yazacaktır.
```
Örneğin:
```python
message = 'My name is Suna'
message = message.replace('Suna','Ayse')  # My name is ayse
```
### 6. split() Metodu
Bu metot bir ayırıcı kullanarak metni bölümlere ayırmak için kullanılır. Yani karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar. 

Örneğin:
```python
message = 'suna'
message = message.split('u') 
print(message) # Ekranda ['s', 'na'] yazar.
```
Örneğin:
```python 
a = "Python,C#,C++,Java"
print(a.split(","))  #  Ekranda [‘Python’, ‘C#’, ‘C++’, ‘Java’] yazacaktır.
```

### 7. input() Metodu
Bu metot kullanılarak kullanıcıdan veri girişi yapması istenir. Aşağıdaki örnek kullanıcı ismini sorar ve ekranda Merhaba … olarak yazdırır.

Örneğin:
```python 
print("Adınız : ")
ad = input()
print("Merhaba, " + ad)
``` 

### String Bir Değer Olup Olmadığını Sorgulamak
Bir ifadenin veri içerisinde geçip geçmediğini anlamak için `in` ve `not in` kullanılır.

Örneğin:
```python 
txt = "Akdeniz Bölgesinde dağlar denize paraleldir"
x = "paralel" in txt
print(x)
y = "paralel" not in txt
print(y)   # kod çalıştırıldığında ekranda x'in True, y'nin False olduğu görülecektir.
```

### String Değerleri Birleştirmek
Metin içeren iki veriyi birleştirmek için `artı (+)` kullanılır.

Örneğin:
```python 
a = "Merhaba"
b = "Dünya!"
c = a + " " + b
print(c)
```

### String Biçimlendirme (Format)
Bunun için `format()` fonksiyonundan faydalanılabilir.

format() yöntemi ile kıvrımlı parantez {} ile ifade edilen yer tutuculara değerler yerleştirir. Bu şekilde farklı türlerde sınırsız değeri metin içerisinde kullanabiliriz.

Örneğin:
```python 
yas = 30
metin = "Benim adım Murat, ve ben {} yaşındayım!"
print(metin.format(yas))   # Ekranda 'Benim adım Murat, ve ben 30 yaşındayım!' yazar.
```
### Kaçış (Escape) Karakteri (\)
Metin yazarken bazı karakterlerin kullanılması sorun yaratabilir. Örneğin içinde üst ayraç (') geçen "Ankara'nın" kelimesini tek tırnak ile ifade ettiğimizde derleyici hata verir.

| Escape Sequence | Usual Interpretation of Character(s) After Backslash  | “Escaped” Interpretation                                     |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| `\'`            | Terminates string with single quote opening delimiter | Literal single quote (`'`) character                         |
| `\"`            | Terminates string with double quote opening delimiter | Literal double quote (`"`) character                         |
| `\<newline>`    | Terminates input line                                 | [Newline is ignored](https://stackoverflow.com/questions/48693600/what-does-the-newline-escape-sequence-mean-in-python) |
| `\\`            | Introduces escape sequence                            | Literal backslash (`\`) character                            |

```python
>>> print('a\
... b\
... c')
abc
```

| Escape Sequence | “Escaped” Interpretation                            |
| --------------- | --------------------------------------------------- |
| `\a`            | ASCII Bell (`BEL`) character                        |
| `\b`            | ASCII Backspace (`BS`) character                    |
| `\f`            | ASCII Formfeed (`FF`) character                     |
| `\n`            | ASCII Linefeed (`LF`) character                     |
| `\N{<name>}`    | Character from Unicode database with given `<name>` |
| `\r`            | ASCII Carriage Return (`CR`) character              |
| `\t`            | ASCII Horizontal Tab (`TAB`) character              |
| `\uxxxx`        | Unicode character with 16-bit hex value `xxxx`      |
| `\Uxxxxxxxx`    | Unicode character with 32-bit hex value `xxxxxxxx`  |
| `\v`            | ASCII Vertical Tab (`VT`) character                 |
| `\ooo`          | Character with octal value `ooo`                    |
| `\xhh`          | Character with hex value `hh`                       |

```python
>>> print("a\tb")
a    b
>>> print("a\141\x61")
aaa
>>> print("a\nb")
a
b
>>> print('\u2192 \N{rightwards arrow}')
→ →
```



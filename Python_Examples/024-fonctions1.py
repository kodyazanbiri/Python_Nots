"""
Değer Tipi (Value Type):
name değişkeni bir değer tipidir. Stringler, tamsayılar gibi temel veri tipleri değer tipleri olarak kabul edilir.
Bu türler, fonksiyona argüman olarak geçirildiğinde, orijinal değişkenin bir kopyası geçirilir ve fonksiyon içindeki değişiklikler orijinal değişkeni etkilemez.
"""
def changeName(n):
    n = 'ada'

name = 'yiğit'

changeName(name)
print(name)  # yiğit

"""
Referans Tipi (Reference Type):
listeler referans tipidir. Listeler gibi karmaşık veri yapıları, fonksiyona argüman olarak geçirildiğinde, orijinal veri yapısının bir referansı (adresi) geçirilir.
Ancak sehirler[:] ile bir kopya geçirildiğinden, fonksiyon içindeki değişiklikler orijinal listeyi etkilemez.
"""
def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']

change(sehirler[:])

print(sehirler)  # ['ankara', 'izmir']

""" -------------Python'da değişken sayıda argüman alabilen bir fonksiyon tanımlayalım
Değişken sayıda argüman almak, bir fonksiyonun çağrıldığında belirli bir sayıdaki argümanla sınırlı olmadan, herhangi bir sayıda argüman kabul edebilmesi anlamına gelir.
Bu, Python'da * operatörü ile gerçekleştirilir ve bu argümanlar bir tuple içinde toplanır. Bu sayede fonksiyonun, kaç argüman alacağını önceden bilmesine gerek kalmaz.
"""
def add(*params):  # Değişken sayıda argüman alabilen bir fonksiyon tanımlanıyor. add fonksiyonu, *params kullanarak değişken sayıda argüman alır. Bu argümanlar bir tuple içinde saklanır.
print(type(params))  # params'ın tipini yazdırıyor, bu tip tuple olacaktır
sum = 0  # Toplamı tutmak için bir değişken tanımlanıyor
for n in params:  # params içindeki her bir argüman için döngü başlatılıyor
  sum = sum + n  # Argümanların değeri sum değişkenine ekleniyor
  return sum  # Toplam değer geri döndürülüyor

print(add(10, 20, 50))  # Fonksiyon üç argümanla çağrılıyor
print(add(10, 20, 30))  # Fonksiyon üç argümanla çağrılıyor
print(add(10, 20, 30,50,60,10,20))  # Fonksiyon yedi argümanla çağrılıyor

 # örnek-------- example fonksiyonu herhangi bir sayıda argüman alabilir. Bu argümanlar params adlı bir tuple içinde toplanır ve döngü ile her biri yazdırılır.
def example(*params):
    for param in params:
        print(param)

example(1, 2, 3)          # 1, 2, 3
example('a', 'b', 'c', 'd')  # 'a', 'b', 'c', 'd'

"""
NOT:
# Tuple oluşur. Bir değişkene birden fazla tipte deger verince Tuple oluşturmuş oluyoruz.
x = 3, 2.0, "mer"
"""

 # ---------  **args, fonksiyonun değişken sayıda anahtar-değer çifti almasını sağlar. args, bir sözlük (dictionary) olacaktır.(2 tane * sözlük yapısını verir)
def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

 # ---------- args'ın tipi (<class 'dict'>) yazdırılır. args.items() ile sözlüğün içindeki her bir anahtar-değer çifti döngüyle gezilir ve format fonksiyonu kullanılarak yazdırılır.
print(type(args))
for key, value in args.items():
    print('{} is {}'.format(key, value))

 # ---------İlk çağrıda üç anahtar-değer çifti sağlanır. İkinci çağrıda dört anahtar-değer çifti sağlanır. Üçüncü çağrıda beş anahtar-değer çifti sağlanır.
displayUser(name='Çınar', age=2, city='istanbul')
displayUser(name='Ada', age=12, city='kocaeli', phone='123132')
displayUser(name='Yiğit', age=14, city='ankara', phone='123132', email='yigit@gmail.com')

# Koleksiyon Veri Tipleri - Dictionaries (Sözlükler)
Python'da dict, ingilizcede sözlük anlamına gelen dictionary'nin kısaltması ile oluşturulmuş bir veriler topluluğudur (dize). Sıralanamaz ancak değiştirilebilir ve anahtarlarla çağırılabilir. Python'da dict oluştururken küme parantezi kullanılır ve her veri bir anahtar ve değerden oluşur. Bu veriler anahtar: değer şeklinde yazılır. Ayrıca veriler arasında mutlaka virgül kullanılır.

Örneğin:
```python
sozluk = {
  "uretici": "Renault",
  "model": "Clio",
  "yil": 2009
}
print(sozluk)
```
### Dict İçerisindeki Verilere Erişmek
Sözlük içindeki nesnelere veri anahtar adını köşeli parantez arasında yazarak erişebilirsiniz:

Örneğin:
```python
x = sozluk["model"]
```
### Ayrıca get() özelliğini kullanarak da veriye erişebilirsiniz.

Örneğin:
```python
x = sozluk.get("model")
```
### Dict İçindeki Değerleri Değiştirmek
Dize içindeki bir nesnenin değerini köşeli parantez arasında referans anahtarını belirtip değiştirebilirsiniz:

Örneğin:
```python
otomobil = {
  "uretici": "Renault",
  "model": "Clio",
  "yil": 2009
}
otomobil["yil"] = 2020;
print(otomobil);
```
### Dict İçerisinde Bulunan Tüm Nesneleri Yazdırmak
Sözlüğümüz içindeki tüm anahtar ve değerleri for döngüsü ile tek tek ele alabiliriz. Dönen değer anahtar adı olacaktır. Ancak anahtardaki veriyi de almanın yöntemi var. Şimdi örnekler üzerinden nesneleri nasıl yazdıracağımıza bakalım:

Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
for x in kisi:
  print(x)   # kod çalıştırıldığı zaman ekrana "Adi", "Soyadi" ve "Yas" anahtarlarının döndüğü görülecektir.
```

Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
for x in kisi:
  print(kisi[x])  # kod çalıştırıldığında bu kez "Murat", "Elicaliskan" ve 37 şeklinde anahtarların değil de değerlerin ekrana yazdırıldığını görürüz.

```

Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
for x in kisi.values():
  print(x)  # Bu örnekte yine verileri elde ettik. Bu kez dict'in values() özelliği ile değerleri çağırıp x değişkenine yükledik ve tek tek yazdırdık.
```


Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
for x, y in kisi.items():
  print(x, y)  #  örnekte hem anahtarları hem değerleri birlikte yazdırdık. Bunun için for döngüsünden sonra x, y kullandık ve dict'in items() özelliğini çağırdık.

```

### Bir Anahtarın Olup Olmadığını Kontrol Etmek
Bunun için "anahtar" in dict yapısını kullanabiliriz.

Örneğin:
```python
otomobil = {
  "uretici": "Ford",
  "model": "Mustang",
  "yil": 1964
}
if "model" in otomobil:
  print("Evet; model, otomobil sözlüğünün bir anahtarıdır")
```
### Sözlüğe Yeni Anahtar Eklemek
dict türü bir nesne içine yeni bir anahtar ve buna karşılık gelen veriyi eklemek için değişken adından hemen sonra köşeli parantez içinde yeni anahtar ve eşittirden sonra değerin yazılması yeterlidir.

Örneğin:
```python
gunler = {
	"Pazartesi": 1,
	"Salı": 2,
	"Çarşamba": 3
}
gunler["Perşembe"] = 4
print(gunler)
```
### Bir Anahtarı Silmek
dict içerisindeki bir anahtarı silmek için pop(anahtar) yapısını kullanırız:

Örneğin:
```python
haftaici = {
	"Pazartesi": 1,
	"Salı": 2,
	"Çarşamba": 3,
	"Perşembe": 4,
	"Cuma": 5,
	"Cumartesi": 6
}
haftaici.pop("Cumartesi")
print(haftaici)
```
Son eklenen nesneyi silmek istiyorsan popitem() özelliğini kullanabiliriz.

### Bir anahtarı silmek için del metodu da kullanılabilir:

Örneğin:
```python
haftaici = {
	"Pazartesi": 1,
	"Salı": 2,
	"Çarşamba": 3,
	"Perşembe": 4,
	"Cuma": 5,
	"Cumartesi": 6
}
del haftaici["Cumartesi"]
print(haftaici)
```
del kullandıktan sonra anahtar belirtmeyip dict adı yazılırsa tüm veriler silinir ve değişken tanımsız (undefined) bir ifade olur.

Örneğin:
```python
haftaici = {
	"Pazartesi": 1,
	"Salı": 2,
	"Çarşamba": 3,
	"Perşembe": 4,
	"Cuma": 5,
	"Cumartesi": 6
}
del haftaici
print(haftaici) # hata verir
```
Eğer bu şekilde sözlük değişkeninin tanımsız bir duruma düşmesini istemiyorsak, sözlük içindeki tüm anahtarları silmek için clear() özelliğini kullanmalıyız.

Örneğin:
```python
haftaici = {
	"Pazartesi": 1,
	"Salı": 2,
	"Çarşamba": 3,
	"Perşembe": 4,
	"Cuma": 5,
	"Cumartesi": 6
}
haftaici.clear()
print(haftaici)
```
### Sözlüğü Kopyalamak
Basit bir şekilde dict1 = dict2 yazarak sözlük kopyalanamaz. Eğer bir sözlüğün aynısından elde etmek istiyorsan copy() özelliğini kullanmalıyız.

Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
yenikisi = kisi.copy()
print(yenikisi)
```
Ayrıca dict nesnesinin yapıcı (constructor) özelliğini kullanarak da bir sözlük başka bir değişkene kopyalanabilir:

Örneğin:
```python
kisi = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan",
	"Yas": 37
}
yenikisi = dict(kisi)
print(yenikisi)
```
### İç İçe Sözlükler
Bir sözlük (dict) içerisinde başka sözlükler kullanabiliriz. Bunu örnek üzerinden anlatalım:

Örneğin:
```python
kisiler = {
	"murat": {
		"Adi": "Murat",
		"Soyadi": "Elicaliskan"
	},
	"yasemin": {
		"Adi": "Yasemin",
		"Soyadi": "Deha"
	}
}
print(kisiler)
```
### Ya da tek tek sözlükler oluşturup bunları tek bir sözlük içinde yazabiliriz:

Örneğin:
```python
murat = {
	"Adi": "Murat",
	"Soyadi": "Elicaliskan"
}
yasemin = {
	"Adi": "Yasemin",
	"Soyadi": "Deha"
}
kisiler = {
	"murat": murat,
	"yasemin": yasemin
}
print(kisiler)
dict Yapıcı (Constructor) Metodu
```
### Sözlük oluşturmak için {"anahtar1":"deger1", "anahtar2":"deger2"} şeklinde kullanmak yerine doğrudan dict nesnesi yaratmamızı sağlayacak yapıcı metodu kullanabiliriz.

Örneğin:
```python
otomobil = dict(uretici="Ford", model="Mustang", yil=1964)
print(otomobil)
```
Bu şekilde sözlükler oluştururken şu iki noktaya dikkat edin: 1- anahtarlar tırnak işaretleri arasında yazılmıyor. 2- iki nokta yerine eşittir kullanılıyor.

NOT: dict'in anahtar sayısını elde etmek için len() fonksiyonu kullanılabilir.


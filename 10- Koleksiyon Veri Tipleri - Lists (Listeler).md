# Koleksiyon Veri Tipleri - Lists (Listeler)
Python Programlama Dilinde 4 tür dize (array) bulunur. 

- Bunlar;
  *  `List `, sıralanabilir ve değiştirilebilir dizeler. Bu tarz dizelere aynı üyeler tekrar eklenebilir.
  *  `Tuple `, sıralanabilir ancak değiştirilemez dizelerdir. Aynı üyeler birden fazla eklenebilir.
  *  `Set ` sıralanamaz ve aynı üyeleri kabul etmez.
  *  `Dictionary ` sıralanamaz ancak değiştirilebilir ve listelenebilir. Aynı üyeler eklenemez.
   
-  Sıralanabilir ve değiştirilebilir veriler topluluğudur. Nesneler köşeli parantezler arasına yazılır.

Örneğin:

```python
thislist = ["elma", "muz", "ayva"]
print(thislist)
```
### Dizedeki Bir Değere Erişmek

Dizedeki bir elemana ulaşmak için sıra numarasını köşeli parantez içinde belirtiriz. İlk elemanın 0 (sıfır) olduğunu unutmayın!

Örneğin:
```python
thislist = ["elma", "muz", "ayva"]
print(thislist[1])  # Ekranda muz yazar.
```
### İki farklı listeyi bir liste içinde gruplamak

Örneğin:
```python
list1 = ['one','two','there']
list2 = ['four','five','six']
```
### Liste içinde farklı listelerde tanımlayabiliriz.
Örneğin:
```python
list1 = [[1,2,3],[4,5,6],[7,8,9],10] # list1 içinde 4 eleman var diyebiliriz ilk 3 eleman bir liste 4.eleman ise number türünde bir değer.
```
- Her bir kullanici bilgisini ayrı bir liste de tanımlayıp sonrasında kullanicilar isminde bir liste içinde gruplama yapabiliriz.

Örneğin:
```python
kullaniciA = ['Suna', 3]
kullaniciB = ['Ayse', 2]

kullanicilar = [kullaniciA,kullaniciB]
```
### Sondan Sıraya Göre Değer Almak
Negatif Sıra: Python'da köşeli parantez içinde negatif sıra numarası belirtebilirsiniz. Bu şekilde kullanıldığında sondan kaçıncı nesne ise o görüntülenecektir.

Örneğin:
```python
thislist = ["elma", "armut", "kiraz"]
print(thislist[-1])
```
### Aralık Belirtmek
Bir dizenin belli elemanlarını aralık belirterek alabilirsiniz. Alınan aralık yeni bir dize olarak dönecektir.

Örneğin:
```python
thislist = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(thislist[2:5])  # Ekranda kiraz, portakal, kivi yazar
```
- Eğer aralık belirtirken ilk sayıyı boş geçersek ilk elemandan belirtilen sayı kadar değeri dize haline dönüştürür.

Örneğin:
```python
liste = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(liste[:4])  # Ekranda elma, muz, kiraz, portakal yazar.
```
- Eğer ikinci parametre boş bırakılırsa bu durumda ilk belirtilen elemandan itibaren dizenin sonuna kadar değerler alınarak bir dize oluşturulur.

Örneğin:
```python
liste = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(liste[2:])  # Ekranda kiraz, portakal, kivi, karpuz, mango yazar.
```
- Negatif sıralar kullanarak bir aralık belirtebiliriz. Örneğin sondan 4. karakterden, sondan 2. karaktere kadar olan değerler seçilecekse, şu tarz bir kod işimizi görecektir:

Örneğin:
```python
liste = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(liste[-4:-1]) # Ekranda portakal, kivi, karpuz yazar.
```
- [::] diyerek tüm listeyi seçmiş oluyoruz.
- 
Örneğin:
```python
liste = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(liste[::]) # Ekranda elma, muz, kiraz, portakal, kivi, karpuz, mango yazar.
```
### Bir Değeri Değiştirmek
Dizedeki bir değeri değiştirmek için önce değişkenin adının sağına köşeli parantez arasında sıra numarası (index) yazılır, ardından eşittir kullanılarak yeni değer yazılır.

Örneğin:
```python
liste = ["elma", "muz", "armut"]
liste[0] = "mandalina"
print(liste)
```
### Listedeki Tüm Elemanları Sırayla Yazdırmak
for döngüsünü aşağıdaki biçimde kullanarak dizedeki değerleri tek tek işleyebiliriz.

 Örneğin:
```python
liste = ["elma", "muz", "kiraz"]
for x in liste:
  print(x)
```
### Bir Değerin Listede Var Olup Olmadığını Kontrol Etmek
Bunun için in komutunu kullanırız. değer in liste sorgusu eğer listede bu değer varsa True, yoksa False olarak döner:

Örneğin:
```python
liste = ["elma", "muz", "kiraz"]
if "elma" in liste
   print("Evet, elma listede var!")
```

### Bir Dizenin Kaç Elemanlı Olduğunu Bulmak
Dizelerin eleman sayısı yani boyutu/genişliği len() fonksiyonu ile tespit edilebilir:

Örneğin:
```python
liste = ["elma", "muz", "kiraz"]
print(len(liste))
```




# Koleksiyon Veri Tipleri - Sets (Kümeler)
Python'da set yine bir dize türüdür. Bu türün özelliği sıralanamaz olmasıdır. Set, bir veri yığınıdır. Ancak bu verilere erişim sıra (index) yoluyla sağlanamamaktadır.

Bir set tanımlarken küme parantezi kullanılır.

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
print(ornekSet)
```
Python List için geçerli özelliklerin çoğu set için de geçerlidir. Aşağıda set'in list'ten farklı yanları belirtilmiştir:

### Nesnelere Erişmek
UYARI: set sıralanamaz olduğu için hangi elemanın hangi sırada olduğu asla bilinemez ve sıra numarası yazılarak elde edilemez.

Ancak for döngüsü ile nesneleri tek tek kontrol edebilir;

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}

for x in ornekSet:
  print(x)
```
### Ya da in sorgusu ile dizede aradığınız değer olup olmadığı öğrenilebilir:

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}

print("muz" in ornekSet)
```

### Set Türü Dizelere Nesne Eklemek
set yığınına veri eklemek için add(nesne) özelliğinden faydalanabilirsiniz:

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
ornekSet.add("portakal")
print(ornekSet)
```
### Birden fazla nesne eklemek için update([nesneler]) özelliğinden faydalanabilirsiniz:

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
ornekSet.update(["portakal", "mango", "üzüm"])
print(ornekSet)
```
### Set Türü Dizelerden Nesne Silmek
Var olan bir elemanı, set yığınından silmek istiyorsak remove(nesne) özelliğini kullanabiliriz:

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
ornekSet.remove("elma")
print(ornekSet)
```
### Eğer silmek istediğimiz nesne yoksa remove() özelliği hata verecektir. Bu nedenle nesnenin dizede olup olmadığından emin değilsek remove() yerine discard() kullanmalıyız:

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
ornekSet.discard("portakal")
print(ornekSet)
```
### pop() özelliğini kullanarak set içindeki son nesne silinebilir. Ancak set'in sıralanamaz olduğunu unutmayın. Yani sildiğiniz nesnenin ne olduğunu bilemezsiniz.

Örneğin:
```python
ornekSet = {"elma", "muz", "kiraz"}
ornekSet.pop()
print(ornekSet)
```
### Set içindeki nesneleri temizlemek için clear(), set'i tamamen kaldırmak ve tanımsız hale getirmek için del kullanılabilir:

Örneğin:
```python
ornekSet = {"apple", "banana", "cherry"}

ornekSet.clear() # tüm nesneleri siler

print(ornekSet) #hata vermez

del ornekSet # tanımsız hale getirir

print(ornekSet) #hata verir
```
### Set Türü Dizeleri Birleştirmek
union() özelliği ile iki set birleştirilerek yeni bir set oluşturulabilir:

Örneğin:
```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
```
### update() özelliği ile bir set içine başka bir set'in değerlerini ekleyebiliriz. Bu durumda yeni bir set oluşmaz. Aşağıdaki örnekte set1'in içine set2'nin nesneleri eklenecektir:

Örneğin:
```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
```
### Yapıcı (Constructor) Kullanarak Set Oluşturmak
Set oluştururken { 1, 2, 3 } şeklinde belirtmek yerine set'in yapıcısını kullanabilirsiniz:

Örneğin:
```python
ornekset = set(("elma", "muz", "kiraz")) # çift parantezli
print(ornekset)  # NOT: set'in eleman sayısını elde etmek için len() fonksiyonu kullanılabilir.
```



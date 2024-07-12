# -------Membership Operator: in
"""
Membership operator (in), bir elemanın bir koleksiyon içinde bulunup bulunmadığını kontrol etmek için kullanılır.
Bu koleksiyonlar genellikle listeler, dizeler, demetler (tuples) veya sözlükler (dictionaries) olabilir. in operatörü, elemanın koleksiyon 
içinde olup olmadığını kontrol eder ve sonuç olarak True veya False döndürür. not in operatörü ise elemanın koleksiyon içinde bulunmadığını kontrol eder. 
"""

x = ['apple', 'banana']
print('banana' in x)  # True döner çünkü 'banana' x listesinde bulunmaktadır.

name = 'Çınar'
print('a' in name)    # True döner çünkü 'a' karakteri name dizisinde bulunmaktadır.
print('a' not in name) # False döner çünkü 'a' karakteri name dizisinde bulunmaktadır.

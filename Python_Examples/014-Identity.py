#------- Identity Operator: is 
"""
Kimlik (identity) operatörü is, Python'da iki değişkenin aynı nesneye (yani aynı bellekteki referansa) işaret edip etmediğini kontrol etmek için kullanılır. 
is operatörü, eşitlik (==) operatöründen farklıdır; çünkü eşitlik operatörü iki değişkenin değerlerinin aynı olup olmadığını kontrol ederken, kimlik operatörü
iki değişkenin aynı nesneyi referans alıp almadığını kontrol eder. 
"""
x = y = [1, 2, 3]  # x ve y aynı referansa sahip
z = [1, 2, 3]      # z ise farklı bir referansa sahip (belleğin farklı bir alanında tutuluyor)

print(x == y)  # x ve y'nin değerleri aynı olduğu için True döner
print(x == z)  # x ve z'nin değerleri de aynı olduğu için True döner

print(x is y)  # x ve y aynı referansa sahip olduğu için True döner(referans kontrolunü is anahtar kelimesi ile yaparız)
print(x is z)  # x ve z farklı referanslara sahip olduğu için False döner


# ORNEK 2---------
x = [1, 2, 3]
y = [2, 4]

# x ve y'nin elemanlarını aynı yapmak için aşağıdaki işlemleri yaptık. artık x ve y'nin elemanları [1, 2] 
del x[2]  # x listesinin üçüncü elemanını (3) sildik. x şimdi [1, 2]
y[1] = 1  # y listesinin ikinci elemanını (4) 1 yaptık. y şimdi [2, 1]
y.reverse()  # y listesinin elemanlarını ters çevirdik. y şimdi [1, 2]

print(x == y)  # True  
print(x is y)  # False
print(x is not y)  # True

# Dairenin alanı ve çevresini hesaplamak için π değerini tanımlıyoruz.
pi = 3.14

# Kullanıcıdan yarıçap değerini alıyoruz ve float türüne dönüştürüyoruz.
r = float(input("Yarı çap: "))

# Dairenin alanını hesaplıyoruz.
alan = pi * (r ** 2)
# Alanın veri türünü kontrol ediyoruz (float).
print(type(alan))

# Dairenin çevresini hesaplıyoruz.
cevre = 2 * pi * r
# Çevrenin veri türünü kontrol ediyoruz (float).
print(type(cevre))

# Hesaplanan alan ve çevreyi ekrana yazdırıyoruz.
print("Alan: " + str(alan) + " Çevre: " + str(cevre))

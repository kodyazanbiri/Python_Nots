# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result1 = (sayi > 0) and (sayi <= 100)
print(f'Sayı 0-100 arasında mı: {result1}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
result2 = (sayi > 0) and (sayi % 2 == 0)
print(f'Girilen sayı pozitif çift sayı mı: {result2}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@XXX.com'
password = 'abc123'

girilenEmail = input('Email: ')
girilenPassword = input('Parola: ')

result3 = (girilenEmail == email) and (girilenPassword == password)
print(f'Uygulamaya giriş başarılı mı: {result3}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result4_a = (a > b) and (a > c)
result4_b = (b > a) and (b > c)
result4_c = (c > a) and (c > b)

print(f'a en büyük sayı mı: {result4_a}')
print(f'b en büyük sayı mı: {result4_b}')
print(f'c en büyük sayı mı: {result4_c}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final: '))

ortalama = ((vize1 + vize2) / 2) * 0.6 + (final * 0.4)
result5 = (ortalama >= 50 and final >= 50) or (final >= 70)

print(f'Öğrencinin ortalaması: {ortalama} ve geçme durumu: {result5}')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4    => Zayıf 
# 18.5-24.9 => Normal  
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)
name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz (metre cinsinden): '))

index = kg / (hg ** 2)
zayif = (0 <= index <= 18.4)
normal = (18.5 <= index <= 24.9)
kilolu = (25 <= index <= 29.9)
obez = (30 <= index <= 34.9)

print(f'{name}, kilo indeksin: {index:.2f} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name}, kilo indeksin: {index:.2f} ve kilo değerlendirmen normal: {normal}')
print(f'{name}, kilo indeksin: {index:.2f} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name}, kilo indeksin: {index:.2f} ve kilo değerlendirmen obez: {obez}')

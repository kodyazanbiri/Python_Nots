
# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1 = float(input('1. vize: '))
# vize2 = float(input('2. vize: '))
# final = float(input('final : '))

# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input('sayı: '))

# tekcift = (sayi % 2 == 0)

# print(f'girilen sayı çift olma durumu: {tekcift}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

# sayi = int(input('sayı: '))
# pozitifmi = (sayi > 0)

# print(f'girilen sayının pozitif olma durumu: {pozitifmi}')

# 5- Kullanıcıdan kullanıcı adı ve şifre bilgisi isteyip doğruluğunu kontrol ediniz. (kullanici: johndoe parola: mypassword)
kullanici = 'johndoe'
sifre = 'mypassword'

girilenKullanici = input('Kullanıcı adı: ')
girilenSifre = input('Şifre: ')

isKullanici = (kullanici == girilenKullanici.lower().strip())
isSifre = (sifre == girilenSifre)

print(f'Kullanıcı adı doğru mu: {isKullanici} ve Şifre doğru mu: {isSifre}')

import datetime

# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#    Ehliyet alma koşulu en az 18 yaşında olmak ve eğitim durumunun lise ya da üniversite olması gerekmektedir.

# Kullanıcıdan gerekli bilgileri alıyoruz
isim = input('İsminiz: ')
yas = int(input('Yaşınız: '))
egitim = input('Eğitim durumunuz (lise/üniversite): ')

# Ehliyet alma koşullarını kontrol ediyoruz
if yas >= 18:
    if egitim.lower() in ['lise', 'üniversite']:
        print(f'{isim}, ehliyet alabilirsiniz.')
    else:
        print(f'{isim}, ehliyet alamazsınız. Eğitim durumunuz yetersiz.')
else:
    print(f'{isim}, ehliyet alamazsınız. Yaşınız tutmuyor.')

# 2- Bir öğrencinin 2 yazılı ve 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 - 24  => 0
#    25 - 44  => 1
#    45 - 54  => 2
#    55 - 69  => 3
#    70 - 84  => 4
#    85 - 100 => 5

# Kullanıcıdan notları alıyoruz
yazili1 = float(input('1. yazılı notunuz: '))
yazili2 = float(input('2. yazılı notunuz: '))
sozlu = float(input('Sözlü notunuz: '))

# Notların ortalamasını hesaplıyoruz
ortalama = (yazili1 + yazili2 + sozlu) / 3

# Ortalamaya göre not aralığını belirliyoruz
if 0 <= ortalama < 25:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 0')
elif 25 <= ortalama < 45:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 1')
elif 45 <= ortalama < 55:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 2')
elif 55 <= ortalama < 70:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 3')
elif 70 <= ortalama < 85:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 4')
elif 85 <= ortalama <= 100:
    print(f'Ortalamanız: {ortalama:.2f}, Notunuz: 5')
else:
    print('Yanlış bilgi girdiniz.')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    datetime modülünü kullanmanız gerekiyor.  
#    Örnek: (simdi) - (2018/8/1) => gün farkı

# Kullanıcıdan aracın trafiğe çıkış tarihini alıyoruz
tarih = input('Aracınız hangi tarihte trafiğe çıktı (yyyy/mm/dd): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

# Şu anki tarihi alıyoruz
simdi = datetime.datetime.now()

# Tarihler arasındaki farkı hesaplıyoruz
fark = simdi - trafigeCikis
days = fark.days

# Gün bazlı farkı yıllara çevirerek servis aralığını belirliyoruz
if days <= 365:
    print('1. servis aralığı')
elif 365 < days <= 365 * 2:
    print('2. servis aralığı')
elif 365 * 2 < days <= 365 * 3:
    print('3. servis aralığı')
else:
    print('Hatalı süre.')

"""NOT:
egitim.lower() ifadesi, kullanıcının girdiği eğitim bilgisini tamamen küçük harfe dönüştürmek için kullanılmıştır. 
Bu sayede, kullanıcı eğitim bilgisini büyük harflerle veya karışık şekilde yazsa bile (örneğin, "Lise", "LİSE", "Ünİversİte" vb.), 
program girdiyi küçük harflere dönüştürerek tutarlı bir karşılaştırma yapabilir.
"""

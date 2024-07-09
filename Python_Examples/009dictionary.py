# Key - Value örneği: Plaka kodları ve şehirler

# Şehirlerin plaka kodlarını içeren sözlük
plakalar = {
    'kocaeli': 41,
    'istanbul': 34
}

# Şehirlerin plaka kodlarını yazdırma
print(plakalar['kocaeli'])   # 41
print(plakalar['istanbul'])  # 34

# Yeni şehir ekleme ve mevcut bir şehir plakasını güncelleme
plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'

# Güncellenmiş plaka sözlüğünü yazdırma
print(plakalar)

# Kullanıcı bilgilerini içeren sözlük
users = {
    'suna': {
        'age': 36,
        'roles': ['user'],
        'email': 'suna@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'ayse': {
        'age': 2,
        'roles': ['admin', 'user'],
        'email': 'ayse@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

# cinarturan kullanıcısının ilk rolünü yazdırma
print(users['suna']['roles'][0])  # admin

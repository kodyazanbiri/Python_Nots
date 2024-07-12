numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 1- Numbers listesindeki hangi sayılar 4'ün katıdır?
for number in numbers:
    if number % 4 == 0:
        print(f'{number} is a multiple of 4')

# 2- Numbers listesinde sayıların toplamı kaçtır?
total = 0
for number in numbers:
    total += number
print('Toplam:', total)

# 3- Numbers listesindeki çift sayıların karesini alınız.
for number in numbers:
    if number % 2 == 0:
        print(f'{number} squared is {number ** 2}')


cities = ['Berlin', 'Paris', 'Madrid', 'Rome', 'Oslo']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
for city in cities:
    if len(city) <= 5:
        print(f'{city} has 5 or fewer characters')

products = [
    {'name': 'iPhone 11', 'price': '5000'},
    {'name': 'iPhone 12', 'price': '6000'},
    {'name': 'iPhone 13', 'price': '7000'},
    {'name': 'iPhone 14', 'price': '8000'},
    {'name': 'iPhone 15', 'price': '9000'}
]

# 5- Ürünlerin fiyatları toplamı nedir?
total_price = 0
for product in products:
    price = int(product['price'])
    total_price += price
print('Toplam ürün fiyatı:', total_price)

# 6- Ürünlerden fiyatı en fazla 7000 olan ürünleri gösteriniz.
for product in products:
    if int(product['price']) <= 7000:
        print(f"{product['name']} is priced at {product['price']} or less")

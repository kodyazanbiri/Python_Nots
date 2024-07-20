def greet(name='user'):
    return f'Hello {name}'

# İlk çağrı, 'Efe' için
msg = greet('Efe')
print(msg)  # Hello Efe

# İkinci çağrı, 'Mira' için
msg = greet('Mira')
print(msg)  # Hello Mira

def sum_numbers(num1, num2):
    return num1 + num2

# İlk toplam hesaplaması
result = sum_numbers(10, 20)
print(result)  # 30

# İkinci toplam hesaplaması
result = sum_numbers(15, 20)
print(result)  # 35

def calculate_age(birth_year, current_year=2023):
    return current_year - birth_year

# Efe, Mira ve Deniz için yaş hesaplamaları
age_efe = calculate_age(2018)
age_mira = calculate_age(2011)
age_deniz = calculate_age(2000)

print(age_efe, age_mira, age_deniz)  # 5 12 23

def years_until_retirement(birth_year, name, current_year=2023):
    '''
    DOCSTRING: Given birth year, calculates years left until retirement.
    INPUT: birth_year (int), name (str)
    OUTPUT: prints years left until retirement or retirement status
    '''
    age = calculate_age(birth_year, current_year)
    retirement_age = 65
    years_left = retirement_age - age

    if years_left > 0:
        print(f'{name}, you have {years_left} years left until retirement.')
    else:
        print(f'{name}, you are already retired.')

years_until_retirement(1983, 'Ali')
years_until_retirement(1950, 'Ahmet')
years_until_retirement(1974, 'Yağmur')

print(help(years_until_retirement))

my_list = [1, 2, 3]
print(help(my_list.append))

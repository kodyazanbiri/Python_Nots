# listeler, dizeler, demetler ve sözlükler üzerinde for döngüsü
# Bir liste üzerinden iterasyon yapma
fruits = ['apple', 'banana', 'cherry', 'date']

for fruit in fruits:
    print(f'I like {fruit}')

# İsimler listesi üzerinde iterasyon yapma
cities = ['New York', 'Los Angeles', 'Chicago']

for city in cities:
    print(f'I would like to visit {city}')

# Bir string üzerinde iterasyon yapma
sentence = 'Hello World'

for char in sentence:
    print(char)

# Bir tuple listesi üzerinde iterasyon yapma
coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]

for x, y in coordinates:
    print(f'X: {x}, Y: {y}')

# Bir dictionary üzerinde iterasyon yapma
student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}

for student, grade in student_grades.items():
    print(f'{student} got grade {grade}')

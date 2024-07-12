# username, password => database

# 'johndoe' , 'abcdef'

x, y, z, w = 8, 8, 15, 3

password = 'abcdef'
username = 'johndoe'

result = (x == y)  # True
result = (x == z)  # False
result = ('jndoe' == username)  # False
result = ('johndoe' == username)  # True
result = (x != y)  # False
result = (x != z)  # True
result = (x > z)  # False
result = (x < z)  # True
result = (x >= y)  # True
result = (z <= y)  # False
result = (True == 1)  # True
result = (False == 0)  # True
result = False + True + 25  # 26

print(result)

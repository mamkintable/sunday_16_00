# Пример создания "скелета" и вызыва функции
def max_from_2(a, b):
    if a < b:
        return b
    else:
        return a

name1 = int(input())
name2 = int(input())

print("max number = ", max_from_2(name1, name2))

# Пример lambda функции
storona_1 = int(input())
storona_2 = int(input())
storona_3 = int(input())
#perimetr = (lambda x, y, z: x + y + z)(storona_1,storona_2,storona_3)
per_treyg = lambda x, y, z: x + y + z
perimetr = per_treyg(storona_1,storona_2,storona_3)
print(perimetr)
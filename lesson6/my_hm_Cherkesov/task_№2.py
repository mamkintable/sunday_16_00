a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = 0
for i in range(a,b+1):
    if i % 2 == 1:
        c += i
print(c)

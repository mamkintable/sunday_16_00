n = int(input("Введите чилос : "))
i = 2
while i <= n:
    i = i + 1
    if n % i == 0:
        print(i)
        break

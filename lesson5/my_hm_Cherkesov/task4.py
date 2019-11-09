n = int(input("Введите число: "))
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for c in range(2, n + 1):
        a, b = b, a + b
    print(b)

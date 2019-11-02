def arithmetic(a,b,c):
    if c == "*":
        print(a*b)
    elif c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "//":
        print(a/b)
    else:
        print("Неизвестная строка")

arithmetic(2,2,"*")

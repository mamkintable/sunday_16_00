def season(month):
    if month == 1 or 2 or 12:
        print ("Это зимний месяц")
    elif month == 3 or 4 or 5:
        print ("Это весенний месяц")
    elif month == 6 or 7 or 8:
        print ("Это летний месяц")
    elif month == 9 or 10 or 11:
        print ("Это осенний месяц")
season(int(input("Введите номер месяца: ")))

a = int(input("apple or orange 1 or 2"))
if a==1: 
    a1 = int(input("GTX 1070 or GTX 1050 1 or 2"))
    if a1==1: 
        print("ВЫ ПРОШЛИ")
    elif a1==2:
        print("ВЫ НЕ ПРОШЛИ")
    else:
        print("2 dol")
elif a==2:
    a1 = int(input("Заказать сборку or Собрать самому 1 or 2"))
    if a1==1: 
        print("ВЫ НЕ ПРОШЛИ")
    elif a1==2:
        print("ВЫ ПРОШЛИ")
    else:
        print("2 dol")
else:
    print("()_()")
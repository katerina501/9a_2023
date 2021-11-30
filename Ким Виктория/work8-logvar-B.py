print("Введите трехзначное число")
a=int(input())
b=a//100
c=a%10
o=(b==c)
if o:
    print("да")
else:
    print("нет")

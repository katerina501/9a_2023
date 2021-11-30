print("Введите 3 значное число")
a =float(input())
s = a//100
b = a//10
c = a%10
d = b%10
print(s)
print(d)
print(c)
if d==c and d==s and c==s:
    print("да")
else:
    print("нет")
    

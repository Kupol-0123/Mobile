print("Реши задачи:")
print("1. Чему равна *,если 11! = 3*916800?  (+2б)")
print("а)4  б)8  в)9  г)0")
print()
b= int(0)
a= int(input("Ответ(Напиши цифру): "))
if a== 9:
    b= b+2
    v= 1
else:
    v= 0
print()
print("2. Реши уровнение(За каждое уровнение +1б):")
print("а) 78-12*x=18 ")
i= int(input("Ответ: "))
m= int(0)
if i== 5:
    b= b+1
    m= 1
else:
    m= 0
print("б) 36:x-9=3")
K= int(input("Ответ: "))
p= int(0)
if K== 3:
    b= b+1
    p= 1
else:
    p= 0
print("в) (108-x):5=20")
V= int(input("Ответ: "))
t= int(0)
if V== 8:
    b= b+1
    t= 1
else:
    t= 0
print("г) x:5+95=106")
n= int(input("Ответ: "))
o= int(0)
if n== 55:
    b= b+1
    o= 1
else:
    o= 0
print()
print("3. Чему равна 10.8:2.4? (+1б)")
print("а)4.1  б)1.9  в)3.5  г)4.5")
print()
q= float(input("Ответ(Пиши не букву): "))
j= int(0)
if q== 4.5:
    b= b+1
    j= 1
else:
    j= 0
print()
print(" 4. По реке плыл катер со скоростью 26,5 км/ч, скорость течении реки была 4,5 км/ч. С какой
      скорость катер плыл бы по течению и против течении? (+3б)")
т= int(input("а)По течению реки: "))
ь= int(input("б)Против течении реки: "))
э= int(0)
if т== 30:
    b= b+2
    э= 1
else:
    э= 0

ж= int(0)
if ь== 22:
    b= b+1
    ж= 1
else:
    ж= 0
print()
print("Ответы:")
if v==1:
    print("1. Верно")
else:
    print("1. Неверно")
if m==1:
    print("2. а)Верно")
else:
    print("2. а)Неверно")
if p==1:
    print("2. б)Верно")
else:
    print("2. б)Неверно")
if t==1:
    print("2. в)Верно")
else:
    print("2. в)Неверно")
if o==1:
    print("2. г)Верно")
else:
    print("2. г)Неверно")
if j==1:
    print("3. Верно")
else:
    print("3. Неверно")
if э==1:
    print("4. а)Верно")
else:
    print("4. а)Неверно")
if ж==1:
    print("4. б)Верно")
else:
    print("4. б)Неверно")
print()
print()
print("Решение: ")
print("1.")
print("Сумма цифр равна 3+*+9+1+6+9+0+0=27+*. Значит надо прибавить столько,")
print("чтобы оно делилась на 3 и 9, значит надо прибавить 9 чтобы делилось на 3 и 9")
print("Значить *= 9")
print()
print()
print("2.")
print("а) 78-12*x=18")
print("   12*x=78-18")
print("   12*x=60")
print("   x=60:12")
print("   x=5")
print()
print("б) 36:x-9=3")
print("   36:x=3+9")
print("   36:x=12")
print("   x=36:12")
print("   x=3")
print()
print("в) (108-x):5=20")
print("    108-x=20*5")
print("    108-x=100")
print("    x=108-100")
print("    x=8")
print()
print("г) x:5+95=106")
print("   x:5=106-95")
print("   x:5=11")
print("   x=11*5")
print("   x=55")
print()
print()
print("3.")
print("10,8:2,4=4,5")
print()
print()
print("4.")
print("1) 26,5+4,5=30км/ч по течению реки")
print("2) 26,5-4,5=22км/ч против течению реки")
print()
print()
print("Итого: ",b,"/ 10 баллов")
if 8<b<11:
    print("Оценка: 5")
else:
    if 6<b<9:
        print("Оценка: 4")
    else:
        if 4<b<7:
            print("Оценка: 3")
        else:
            if b<3:
                print("Оценка: 2")
